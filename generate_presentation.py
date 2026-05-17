#!/usr/bin/env python3
"""
Generate a PowerPoint presentation for the TODO App Azure deployment
Requirements: pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def add_title_slide(prs, title, subtitle):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(52, 152, 219)  # Blue
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.paragraphs[0].font.size = Pt(54)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    
    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.8), Inches(9), Inches(1))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = subtitle
    subtitle_frame.paragraphs[0].font.size = Pt(28)
    subtitle_frame.paragraphs[0].font.color.rgb = RGBColor(236, 240, 241)

def add_content_slide(prs, title, content_list):
    """Add a content slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # White background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # Title box
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.paragraphs[0].font.size = Pt(40)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = RGBColor(52, 152, 219)
    
    # Add blue line under title
    line = slide.shapes.add_shape(1, Inches(0.5), Inches(1.3), Inches(9), Inches(0))
    line.line.color.rgb = RGBColor(52, 152, 219)
    line.line.width = Pt(3)
    
    # Content
    content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(8.4), Inches(4.5))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True
    
    for i, item in enumerate(content_list):
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()
        
        p.text = item
        p.level = 0
        p.font.size = Pt(18)
        p.font.color.rgb = RGBColor(44, 62, 80)
        p.space_before = Pt(6)
        p.space_after = Pt(6)

def add_two_column_slide(prs, title, left_content, right_content):
    """Add a slide with two columns"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # White background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.paragraphs[0].font.size = Pt(40)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = RGBColor(52, 152, 219)
    
    # Left column
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.2), Inches(4.5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True
    for i, item in enumerate(left_content):
        if i == 0:
            p = left_frame.paragraphs[0]
        else:
            p = left_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(44, 62, 80)
        p.space_after = Pt(6)
    
    # Right column
    right_box = slide.shapes.add_textbox(Inches(5.3), Inches(1.5), Inches(4.2), Inches(4.5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True
    for i, item in enumerate(right_content):
        if i == 0:
            p = right_frame.paragraphs[0]
        else:
            p = right_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(44, 62, 80)
        p.space_after = Pt(6)

def create_presentation():
    """Create the full presentation"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Slide 1: Title
    add_title_slide(prs, "Advanced TODO App", "Full-Stack Deployment to Azure Cloud")
    
    # Slide 2: Project Objectives
    add_content_slide(prs, "Project Objectives", [
        "✓ Build a production-ready full-stack application",
        "✓ Master containerization with Docker",
        "✓ Deploy to Kubernetes on Azure AKS",
        "✓ Implement CI/CD pipeline with GitHub Actions",
        "✓ Learn Infrastructure as Code with Azure Bicep",
        "✓ Understand real-time collaboration features"
    ])
    
    # Slide 3: Technology Stack
    add_two_column_slide(prs, "Technology Stack", 
        [
            "Frontend:",
            "• React 18 with TypeScript",
            "• Tailwind CSS for styling",
            "• Axios for HTTP requests",
            "• WebSocket for real-time updates"
        ],
        [
            "Backend:",
            "• Node.js + Express.js",
            "• Prisma ORM",
            "• JWT authentication",
            "• PostgreSQL database"
        ])
    
    # Slide 4: DevOps & Infrastructure
    add_two_column_slide(prs, "DevOps & Cloud Architecture",
        [
            "Containerization:",
            "• Docker for all components",
            "• Multi-stage builds",
            "• Optimized image sizes"
        ],
        [
            "Azure Services:",
            "• AKS (Kubernetes cluster)",
            "• Container Registry (ACR)",
            "• Managed PostgreSQL",
            "• Key Vault for secrets"
        ])
    
    # Slide 5: Application Architecture
    add_content_slide(prs, "Application Architecture", [
        "Frontend Layer: React SPA with real-time WebSocket support",
        "Backend Layer: Express.js API with authentication & authorization",
        "Database Layer: PostgreSQL with Prisma ORM for data persistence",
        "Real-time Layer: WebSocket server for live todo updates",
        "Authentication: JWT tokens with role-based access control"
    ])
    
    # Slide 6: Database Schema
    add_content_slide(prs, "Database Schema", [
        "Users: User accounts with roles (ADMIN, USER)",
        "Teams: Groups for collaboration with team members",
        "Todos: Tasks with priority, due dates, and assignees",
        "Features: Cascading deletes, unique constraints, auto-timestamps",
        "Security: Row-level access control through team membership"
    ])
    
    # Slide 7: Kubernetes Deployment
    add_two_column_slide(prs, "Kubernetes Deployment",
        [
            "What's Deployed:",
            "• PostgreSQL container",
            "• Backend API (3 replicas)",
            "• Frontend (3 replicas)",
            "• Nginx ingress controller",
            "• Secrets & ConfigMaps"
        ],
        [
            "AKS Features:",
            "• Auto-scaling (HPA)",
            "• Load balancing",
            "• Health checks",
            "• Persistent volumes",
            "• Private networking"
        ])
    
    # Slide 8: CI/CD Pipeline
    add_content_slide(prs, "GitHub Actions CI/CD Pipeline", [
        "1. Test Phase: Run unit tests, linting on all PRs",
        "2. Build Phase: Build Docker images on main branch",
        "3. Push Phase: Push to Azure Container Registry",
        "4. Deploy Phase: Apply Kubernetes manifests to AKS",
        "5. Security: Automated vulnerability scanning"
    ])
    
    # Slide 9: Azure Resources
    add_content_slide(prs, "Azure Resources Created", [
        "✓ Azure Kubernetes Service (AKS) - Cluster management",
        "✓ Azure Container Registry (ACR) - Image storage",
        "✓ Azure Database PostgreSQL - Managed database",
        "✓ Azure Key Vault - Secrets management",
        "✓ Application Insights - Performance monitoring",
        "✓ Log Analytics - Centralized logging"
    ])
    
    # Slide 10: Deployment Steps
    add_content_slide(prs, "Step-by-Step Deployment", [
        "1. Setup Azure Subscription & Resource Group",
        "2. Run Bicep templates to create infrastructure",
        "3. Build & push Docker images to ACR",
        "4. Create GitHub repository & add secrets",
        "5. Deploy application to AKS using kubectl",
        "6. Configure DNS and SSL certificates",
        "7. Monitor with Application Insights"
    ])
    
    # Slide 11: Local Development
    add_content_slide(prs, "Local Development Setup", [
        "Prerequisites: Docker, Node.js, npm installed",
        "1. Clone repository",
        "2. Copy .env.example to .env",
        "3. Run: docker compose up",
        "4. Frontend: http://localhost:3000",
        "5. Backend: http://localhost:5000",
        "6. Database: localhost:5432"
    ])
    
    # Slide 12: Feature Highlights
    add_two_column_slide(prs, "Feature Highlights",
        [
            "User Features:",
            "• Create & manage todos",
            "• Set priorities & due dates",
            "• Real-time updates",
            "• Team collaboration"
        ],
        [
            "Admin Features:",
            "• User management",
            "• Team management",
            "• Role-based access",
            "• Activity monitoring"
        ])
    
    # Slide 13: Scaling & Performance
    add_content_slide(prs, "Scaling & Performance", [
        "Horizontal Scaling: Kubernetes auto-scaling based on CPU/memory",
        "Load Balancing: Azure Load Balancer distributes traffic",
        "Database: PostgreSQL with connection pooling",
        "Caching: CDN for frontend assets",
        "Monitoring: Real-time metrics via Application Insights"
    ])
    
    # Slide 14: Security Best Practices
    add_content_slide(prs, "Security Implementation", [
        "✓ JWT authentication for API endpoints",
        "✓ Role-based access control (RBAC)",
        "✓ TLS/SSL encryption in transit",
        "✓ Secrets stored in Azure Key Vault",
        "✓ Network isolation with VPC",
        "✓ Vulnerability scanning with Trivy"
    ])
    
    # Slide 15: Cost Optimization
    add_content_slide(prs, "Azure Cost Optimization", [
        "AKS Cluster: Auto-scaling reduces idle costs",
        "Database: Managed PostgreSQL reduces operations overhead",
        "Container Registry: Standard tier for production workloads",
        "Monitoring: Application Insights with reserved capacity",
        "Storage: Persistent volumes on managed disks",
        "Estimated: $150-300/month for production setup"
    ])
    
    # Slide 16: Key Learnings
    add_content_slide(prs, "Key Learnings & Skills", [
        "✓ Full-stack application development",
        "✓ Containerization & Docker best practices",
        "✓ Kubernetes orchestration",
        "✓ Infrastructure as Code with Bicep",
        "✓ CI/CD pipeline automation",
        "✓ Cloud architecture design",
        "✓ Production deployment strategies"
    ])
    
    # Slide 17: Next Steps
    add_content_slide(prs, "Next Steps & Improvements", [
        "→ Add more API endpoints (filtering, searching)",
        "→ Implement user notifications system",
        "→ Add backup & disaster recovery",
        "→ Implement API rate limiting",
        "→ Add multi-region deployment",
        "→ Implement GraphQL for flexible queries"
    ])
    
    # Slide 18: Resources & Documentation
    add_content_slide(prs, "Resources & Documentation", [
        "📖 README.md - Project overview",
        "📖 QUICKSTART.md - Getting started guide",
        "📖 CICD.md - CI/CD pipeline details",
        "📖 infrastructure/README.md - Azure setup",
        "📖 k8s/README.md - Kubernetes deployment",
        "🔗 GitHub Repository: Main source of truth"
    ])
    
    # Slide 19: Q&A
    add_title_slide(prs, "Questions & Answers", "Understanding the Complete Deployment Journey")
    
    # Save presentation
    output_path = "/Users/admin/TODOAPP/TODO_App_Azure_Deployment.pptx"
    prs.save(output_path)
    print(f"✅ Presentation created: {output_path}")

if __name__ == "__main__":
    create_presentation()
