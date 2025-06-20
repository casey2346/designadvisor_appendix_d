# DesignAdvisor Appendix D

This folder contains experimental configurations for Tracks A–C as described in Appendix D of the paper.

## Structure

- `prompts/`: Role-specific prompt templates (JSON)  
  └── e.g., `compliance_officer.json`

- `logs/`: Multi-agent interaction logs in `.jsonl` format  
  └── e.g., `trackA_session1.jsonl`

- `scripts/`: Evaluation scripts for consensus rounds and JS divergence  
  └── e.g., `evaluation.py`

# DesignAdvisor Evaluation Scripts
This folder contains prompt templates, deliberation logs, and analysis scripts corresponding to Appendix D in our paper. Run `scripts/evaluation.py` to reproduce the JS divergence metric reported in Section 5.


## OpenAI API Configuration

- Version: `2024-12`  
- Temperature: `0.3`  
- Max Tokens: `2048`
