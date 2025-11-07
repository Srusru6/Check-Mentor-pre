REPORT_TEMPLATE = """
基于以下{num_papers}篇论文的分析结果，生成一份关于{aspect}的综合报告：

{paper_analysis}

请生成一份300字左右的分析报告，重点说明以下方面：
1. 总体趋势和特点
2. 具体论据支撑
3. 对本科生的建议

注意：
- 保持客观专业的语气
- 给出具体的例证
- 结论要有实际指导意义
"""

FINAL_SYNTHESIS_TEMPLATE = """
# 关于{professor_name}教授的学术研究分析报告

---

## 1. 核心研究贡献与方向

### **综合评述**
{contribution_summary}

### **关键贡献一览**
{contribution_details}

---

## 2. 所处领域的热点问题

### **综合评述**
{field_problems_summary}

### **热点问题一览**
{field_problems_details}

---

## 3. 本科生科研项目建议

### **综合评述**
{undergrad_projects_summary}

### **项目点子一览**
{undergrad_projects_details}

---
*这份报告由AI根据提供的论文数据自动生成，旨在提供一个高度凝练的学术快照，仅供参考。*
"""


