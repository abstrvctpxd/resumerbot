from datetime import datetime


def generate_proposal(job_posting):
    """Generate a job proposal from a job posting."""
    return {
        'title': 'Job Proposal',
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'job_posting': job_posting,
        'proposal_body': _create_proposal_body(job_posting),
    }


def _create_proposal_body(job_posting):
    """Create proposal body from job posting."""
    return f"""
Dear Project Owner,

Thank you for considering this proposal in response to your job posting.

JOB POSTING SUMMARY:
{job_posting}

PROPOSAL:
Based on the requirements outlined above, I am prepared to:

1. Deliver high-quality work aligned with your specifications
2. Meet all agreed-upon timelines and milestones
3. Maintain clear communication throughout the project
4. Provide professional and thorough implementation

NEXT STEPS:
Please review this proposal and let me know if you would like to discuss:
- Project timeline and deliverables
- Pricing and payment terms
- Technical specifications and requirements

I look forward to hearing from you.

Best regards,
Your Name
"""
