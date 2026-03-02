"""
Modelos de datos para el sistema multi-agente de heru.app
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal
from enum import Enum
from datetime import datetime
import uuid


class AgentRole(str, Enum):
    ORCHESTRATOR = "orchestrator"
    LEAD_QUALIFIER = "lead_qualifier"
    COPYWRITER = "copywriter"
    GRAPHIC_DESIGNER = "graphic_designer"
    SOCIAL_LISTENER = "social_listener"
    PERFORMANCE_ADS = "performance_ads"
    BUSINESS_ANALYST = "business_analyst"
    SAT_INTELLIGENCE = "sat_intelligence"


class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    type: str
    description: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    assigned_to: Optional[AgentRole] = None
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM
    result: Optional[Any] = None
    error: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    metadata: Optional[Dict] = None


class AgentResponse(BaseModel):
    agent: AgentRole
    task_id: str
    result: str
    success: bool = True
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    next_actions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class LeadProfile(BaseModel):
    """Perfil de un lead de ventas de heru"""
    name: Optional[str] = None
    occupation: Optional[str] = None
    platform: Optional[str] = None  # Uber, Rappi, Freelance, etc.
    monthly_income_range: Optional[str] = None
    has_rfc: Optional[bool] = None
    has_sat_issues: Optional[bool] = None
    currently_uses_contador: Optional[bool] = None
    lead_score: Optional[int] = Field(default=None, ge=0, le=100)
    segment: Optional[str] = None
    recommended_plan: Optional[str] = None
    urgency_level: Optional[str] = None
    next_action: Optional[str] = None
    notes: Optional[str] = None


class ContentRequest(BaseModel):
    """Solicitud de contenido para el copywriter"""
    platform: Literal["instagram", "facebook", "tiktok", "linkedin", "email", "ads"]
    content_type: str  # educativo, pain_point, social_proof, producto, temporada
    objective: str  # awareness, conversión, educación, engagement
    topic: str
    target_segment: Optional[str] = None
    campaign_name: Optional[str] = None
    special_instructions: Optional[str] = None


class VisualRequest(BaseModel):
    """Solicitud de contenido visual para el diseñador"""
    platform: str
    piece_type: str  # carrusel, infografia, meme, foto_producto, ad_creativo
    copy: Optional[str] = None  # copy que acompañará la imagen
    objective: str
    visual_style: Optional[str] = None
    color_scheme: Optional[str] = None
    dimensions: Optional[str] = None
    special_requirements: Optional[str] = None


class SocialListeningRequest(BaseModel):
    """Solicitud de social listening"""
    query_type: str  # brand_mention, competitor, trend, lead_opportunity, crisis
    platforms: List[str] = Field(default_factory=list)
    time_range: str = "last_7_days"
    include_sentiment: bool = True
    include_competitors: bool = False
    keywords: List[str] = Field(default_factory=list)


class AdsReportRequest(BaseModel):
    """Solicitud de reporte de ads"""
    report_type: Literal["daily", "weekly", "monthly", "custom"]
    platforms: List[str] = Field(default_factory=lambda: ["google", "meta"])
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    include_recommendations: bool = True
    include_forecast: bool = False
    campaigns: Optional[List[str]] = None  # Si None, reporta todas


class OrchestrationPlan(BaseModel):
    """Plan de orquestación para tareas complejas"""
    original_request: str
    analysis: str
    steps: List[Dict[str, Any]] = Field(default_factory=list)
    agents_involved: List[AgentRole] = Field(default_factory=list)
    execution_order: str = "sequential"  # sequential | parallel
    expected_outputs: Dict[str, str] = Field(default_factory=dict)
