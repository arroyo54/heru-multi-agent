"""
Conectores de datos para Social Listening de heru.app.

Dos tracks de monitoreo:
  TRACK A — Brand: qué dice la gente DE heru
  TRACK B — Ecosystem: qué habla la gente sobre impuestos, SAT, RESICO, freelancers, drivers

Sin costo:
  Reddit  → API JSON pública (sin credenciales)
  YouTube → YouTube Data API v3 (gratis, usa GOOGLE_API_KEY)
El resto usa Apify.
"""
import os
import time
import requests
from datetime import datetime, timedelta
from typing import Optional
from apify_client import ApifyClient


# ─── Queries — TRACK A: Brand monitoring ─────────────────────────────────────

BRAND_QUERIES = {
    "twitter":   ["heru.app", "@heru_app", "@herumx", "heru impuestos"],
    "tiktok":    ["heruapp", "herumx"],
    "instagram": ["heruapp", "herumx"],
}

# ─── Queries — TRACK B: Ecosystem listening ───────────────────────────────────

ECOSYSTEM_QUERIES = {
    "twitter": [
        "RESICO impuestos mexico",
        "SAT freelancer mexico",
        "declaracion impuestos uber mexico",
        "como declarar rappi mexico",
        "me cambiaron RESICO no se que hacer",
        "miedo SAT multa freelancer",
        "impuestos plataformas digitales mexico",
        "cuanto pago de impuestos siendo freelancer mexico",
    ],
    "tiktok": [
        "satmexico",
        "impuestosmexico",
        "freelancermexico",
        "RESICO",
        "impuestosfreelancer",
        "trabajadorindependiente",
    ],
    "instagram": [
        "satmexico",
        "freelancermexico",
        "RESICO",
        "impuestosfreelancer",
        "trabajadorindependiente",
        "ubermexico",
    ],
    "facebook_groups": [
        "https://www.facebook.com/groups/conductoresubermx",
        "https://www.facebook.com/groups/conductoresdidimexico",
        "https://www.facebook.com/groups/rappiconductoresmx",
        "https://www.facebook.com/groups/freelancersmexico",
        "https://www.facebook.com/groups/resicomexico",
    ],
    "youtube": [
        "como declarar impuestos freelancer mexico 2026",
        "RESICO obligaciones SAT mexico",
        "uber impuestos mexico declaracion",
        "miedo SAT multa trabajador independiente",
    ],
    "reddit_subreddits": [
        "mexico", "MexicoFinanciero", "FinanzasPersonales",
        "freelance", "digitalnomad", "mexicoexpats",
        "MexicoCity", "sidehustle", "SATMexico",
    ],
    "reddit_keywords": [
        "SAT", "RESICO", "impuestos", "freelancer",
        "nomada digital", "pagar impuestos Mexico",
        "regimen fiscal", "Uber impuestos",
        "trabajador independiente", "factura Mexico",
    ],
    # Quincenal
    "quora_topics": [
        "como-declarar-impuestos-freelancer-mexico",
        "que-es-resico-mexico",
        "sat-plataformas-digitales",
    ],
}

# ─── Actor IDs de Apify ───────────────────────────────────────────────────────

ACTORS = {
    "twitter":         "apidojo/tweet-scraper",
    "tiktok":          "clockworks/free-tiktok-scraper",
    "instagram":       "apify/instagram-hashtag-scraper",
    "facebook_groups": "apify/facebook-groups-scraper",
    "youtube":         "streamers/youtube-scraper",
    "quora":           "apify/quora-scraper",
}


# ─── Extractor de texto por plataforma ───────────────────────────────────────

def extract_text(item: dict, platform: str) -> str:
    fields = {
        "twitter":         ["text", "fullText", "tweetText"],
        "tiktok":          ["text", "description", "videoDescription"],
        "instagram":       ["caption", "text", "accessibility"],
        "facebook_groups": ["message", "text", "postText", "body"],
        "youtube":         ["title", "description", "snippet_title", "snippet_description"],
        "reddit":          ["title", "selftext", "body"],
        "quora":           ["answer", "question", "text"],
    }
    for field in fields.get(platform, ["text", "body", "title"]):
        val = item.get(field)
        if val and isinstance(val, str) and val.strip():
            return val.strip()[:400]
    return str(item)[:200]


def extract_author(item: dict) -> str:
    for field in ["username", "author", "authorName", "user", "screenName", "displayName"]:
        val = item.get(field)
        if val and isinstance(val, str):
            return val.strip()
    return "usuario"


# ─── Conector Apify ───────────────────────────────────────────────────────────

class ApifyConnector:

    def __init__(self, api_token: Optional[str] = None):
        token = api_token or os.environ.get("APIFY_API_TOKEN")
        if not token:
            raise ValueError("APIFY_API_TOKEN no encontrada en .env")
        self.client = ApifyClient(token)

    def _run(self, actor_id: str, run_input: dict, limit: int) -> list:
        try:
            run = self.client.actor(actor_id).call(run_input=run_input)
            items = []
            for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
                items.append(item)
                if len(items) >= limit:
                    break
            return items
        except Exception as e:
            print(f"  ⚠️  [{actor_id}] {e}")
            return []

    def scrape_twitter(self, queries: list, max_items: int = 50) -> list:
        per_query = max(1, max_items // len(queries))
        results = []
        for q in queries:
            items = self._run(
                ACTORS["twitter"],
                {"searchTerms": [q], "maxTweets": per_query, "queryType": "Latest"},
                limit=per_query,
            )
            results.extend(items)
        return results

    def scrape_tiktok(self, hashtags: list, max_items: int = 40) -> list:
        return self._run(
            ACTORS["tiktok"],
            {"hashtags": hashtags, "resultsPerPage": max_items, "shouldDownloadVideos": False},
            limit=max_items,
        )

    def scrape_instagram(self, hashtags: list, max_items: int = 40) -> list:
        return self._run(
            ACTORS["instagram"],
            {"hashtags": hashtags, "resultsLimit": max_items},
            limit=max_items,
        )

    def scrape_facebook_groups(self, group_urls: list, max_posts: int = 25) -> list:
        return self._run(
            ACTORS["facebook_groups"],
            {
                "startUrls": [{"url": url} for url in group_urls],
                "resultsLimit": max_posts,
                "maxPostComments": 3,
            },
            limit=max_posts,
        )

    def scrape_youtube(self, queries: list, max_results: int = 20) -> list:
        per_query = max(1, max_results // len(queries))
        results = []
        for q in queries:
            items = self._run(
                ACTORS["youtube"],
                {"searchKeywords": q, "maxResults": per_query},
                limit=per_query,
            )
            results.extend(items)
        return results

    def scrape_quora(self, topics: list, max_items: int = 10) -> list:
        results = []
        per_topic = max(1, max_items // len(topics))
        for topic in topics:
            items = self._run(
                ACTORS["quora"],
                {"startUrls": [{"url": f"https://es.quora.com/topic/{topic}"}], "maxItems": per_topic},
                limit=per_topic,
            )
            results.extend(items)
        return results

    @staticmethod
    def is_available() -> bool:
        return bool(os.environ.get("APIFY_API_TOKEN"))


# ─── YouTube Data API v3 (gratis, usa GOOGLE_API_KEY) ────────────────────────

def scrape_youtube(queries: list, max_results: int = 20) -> list:
    """
    Busca videos en YouTube usando la Data API v3 — sin Apify, sin costo.
    Usa GOOGLE_API_KEY del .env. Cuota: 10,000 unidades/día (100 por búsqueda).
    Retorna items normalizados con los mismos campos que extract_text espera.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("  ⚠️  [YouTube] GOOGLE_API_KEY no configurada")
        return []

    results = []
    per_query = max(3, max_results // len(queries))

    for query in queries:
        try:
            resp = requests.get(
                "https://www.googleapis.com/youtube/v3/search",
                params={
                    "key":                api_key,
                    "q":                  query,
                    "part":               "snippet",
                    "type":               "video",
                    "maxResults":         per_query,
                    "order":              "relevance",
                    "relevanceLanguage":  "es",
                    "regionCode":         "MX",
                    "publishedAfter":     _one_week_ago_rfc3339(),
                },
                timeout=10,
            )
            if resp.status_code != 200:
                print(f"  ⚠️  [YouTube] Error {resp.status_code}: {resp.text[:100]}")
                continue

            for item in resp.json().get("items", []):
                snippet = item.get("snippet", {})
                results.append({
                    "title":            snippet.get("title", ""),
                    "description":      snippet.get("description", ""),
                    "username":         snippet.get("channelTitle", ""),
                    "publishedAt":      snippet.get("publishedAt", ""),
                    "videoId":          item.get("id", {}).get("videoId", ""),
                    "_query":           query,
                    "_platform":        "youtube",
                })
            time.sleep(0.5)

        except Exception as e:
            print(f"  ⚠️  [YouTube] query='{query}': {e}")

    return results


def _one_week_ago_rfc3339() -> str:
    from datetime import timezone
    dt = datetime.now(timezone.utc) - timedelta(days=7)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# ─── Conector Reddit (API JSON pública, sin credenciales) ────────────────────

def scrape_reddit(subreddits: list, keywords: list, max_posts: int = 25) -> list:
    """
    Scrapea Reddit usando su endpoint JSON público — sin API key ni Apify.
    Rate limit: 1 request/segundo respetado con sleep.
    """
    headers = {"User-Agent": "heru-social-listener/1.0"}
    results = []
    per_call = max(3, max_posts // (len(subreddits) * min(len(keywords), 3)))

    for sub in subreddits:
        for kw in keywords[:3]:
            try:
                resp = requests.get(
                    f"https://www.reddit.com/r/{sub}/search.json",
                    params={"q": kw, "sort": "new", "t": "week", "limit": per_call},
                    headers=headers,
                    timeout=10,
                )
                if resp.status_code == 200:
                    for post in resp.json()["data"]["children"]:
                        results.append(post["data"])
            except Exception as e:
                print(f"  ⚠️  Reddit r/{sub} q={kw}: {e}")
            time.sleep(1)

    return results
