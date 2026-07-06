from flask import render_template, request, redirect, url_for, flash
from app import app
from app.proposal_generator import generate_proposal


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_posting = request.form.get('job_posting', '')
        owner_email = request.form.get('owner_email', '')
        
        if not job_posting.strip():
            flash('Please paste a job posting', 'error')
            return redirect(url_for('index'))
        
        proposal = generate_proposal(job_posting)
        return render_template('proposal.html', proposal=proposal, owner_email=owner_email)
    
    return render_template('index.html')


@app.route('/send-proposal', methods=['POST'])
def send_proposal():
    proposal_text = request.form.get('proposal_text', '')
    owner_email = request.form.get('owner_email', '')
    
    # For now, just display success message
    # In production: send email here
    flash(f'Proposal queued to send to {owner_email}', 'success')
    return redirect(url_for('index'))
