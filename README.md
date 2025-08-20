# 2024 Customer Retention Analysis

**Author:** Automated PR by LLM tools • **Contact:** 24ds2000041@ds.study.iitm.ac.in

This pull request analyzes quarterly customer retention rates for 2024, visualizes the trend against the industry target (85), and outlines a focused plan to close the gap.

## Data
- **Q1:** 65.08  
- **Q2:** 74.61  
- **Q3:** 73.22  
- **Q4:** 76.13  
- **Average (2024):** **72.26**  
- **Industry Target:** **85**

Data source: `data/retention_2024.csv`

## How to run
```bash
python -m pip install -r requirements.txt
python src/analyze_retention.py
```

The script outputs:
- `plots/trend_vs_target.png`
- `plots/gap_to_target.png`
- `analysis_summary.json` (key stats)

## Key Findings
1. **Upward trajectory, but short of target:** Retention improved from **65.08 (Q1)** to **76.13 (Q4)**, yet the annual **average is 72.26**, which is **12.74 points below** the 85 target.
2. **Volatility mid-year:** Q2 peaked at **74.61**, Q3 dipped to **73.22**, suggesting cohort churn or seasonal friction before recovering in Q4.
3. **Best quarter still below benchmark:** Even the strongest quarter (**Q4 = 76.13**) trails the target by **8.87 points**.

## Business Implications
- **Revenue risk from churn:** Each point below target reflects a sizable revenue delta due to lost renewals and expansion opportunities.
- **Rising CAC pressure:** If retention lags, more spend is required to backfill lost customers to sustain topline growth.
- **Unit economics:** Lower retention suppresses LTV, which can constrain efficient growth and depress margin.

## Recommendations to Reach 85
**Primary solution: implement targeted retention campaigns.** Focus on precise, high-ROI interventions rather than broad discounts.

### 1) Targeted Retention Campaigns (Core Playbook)
- **Cohort micro-segmentation:** Split by tenure (0–3m, 3–6m, 6–12m, 12m+), product usage, industry, and ARR band. Identify top-churn risk cohorts from product telemetry and support logs.
- **Trigger-based outreach:** Launch **in-app nudges** and **email sequences** when usage drops ≥25% week-over-week, or when billing/renewal milestones approach.
- **Persona-specific value messaging:** Map 2–3 most-used outcomes per segment; showcase those wins via templates, playbooks, and short Loom-style walkthroughs.
- **Save offers tied to activation:** Offer limited incentives (credits, feature trials) that **unlock after** the user completes activation steps (e.g., integrates a key workflow) to build durable stickiness.
- **Success pods:** Assign CSM “pods” to the highest-risk deciles to run 30–45 day “save sprints” with weekly standups and clear MBOs (e.g., +4 pts in target cohort).

### 2) Product & Experience Levers
- **Activation friction removal:** Triage top 5 setup blockers (time-to-value > 1 day, missing integrations, confusing defaults). Ship fixes behind feature flags and measure impact on Day-7/Day-30 retention.
- **Habit loops:** Add lightweight weekly value moments (insights email, auto-reports, usage streak badges) to increase return frequency.
- **Risk alerts:** Build a churn-risk score from recency, frequency, depth of use, and support sentiment; surface to CSMs with playbook links.

### 3) Pricing & Contract Levers
- **Anniversary/joint-commit bundles:** Multi-month bundles that trade mild discounts for commit + product adoption actions.
- **Auto-renew protections:** Renewal reminders with click-to-extend and grace windows to reduce involuntary churn.
- **Term optimization:** Encourage quarterly-to-annual upgrades for sticky segments using value framing, not blanket discounts.

### 4) Measurement & Targets
- **North-star:** Raise quarterly retention by **~3–4 pts per quarter** over the next **3 quarters** to hit/approach **85**.
- **Scorecards:** Track cohort retention, feature adoption, activation milestones, and save-rate by campaign.
- **A/B discipline:** Every campaign gets a control group; promote only if net retention lift > 1.5 pts and CAC payback < 9 months.

## Visualizations
See `plots/trend_vs_target.png` and `plots/gap_to_target.png` for the trend and benchmark comparison.

---

_This PR contains analysis code, visualizations, and a data story. For verification, the submitter email is **24ds2000041@ds.study.iitm.ac.in**._
