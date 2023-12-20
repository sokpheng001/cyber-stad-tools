from abc import ABC
from datetime import date
from pathlib import Path
import sqlite3
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from io import BytesIO
import base64
from PIL import Image

class Report(ABC):
    def __init__(self):
        self.data = 'abc'  # Initialize to False or true to check conditions (static)
        self.output_path = Path(__file__).parent / "output" 
        self.output_path.mkdir(parents=True, exist_ok=True)  
 
    def generate_report(self):
        file_name = "report.pdf" 
        if self.data == '': #false
            print("No data available to generate a report, start exploit first.")
        else:
            print(f"Generating report name ---> {file_name} ...")
            
            # Specify the file names for header and content images
            header_file = "header.png"
            diagram_file = "diagram.png"

            pdf = FPDF("P", "mm", "A4")
            pdf.add_page()
            

            # add header image (will be code it later, but let me put the screenshort first)
            pdf.ln(10)
            pdf.image(str(self.output_path / header_file), x=None, y=None, w=pdf.w - 20, h=0)

            # Set font for the Table of Contents
            pdf.add_page()
            pdf.ln(20)
            pdf.set_left_margin(20)
            pdf.set_right_margin(20) 
            
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color

            # Add "Table of Contents" text
            pdf.cell(0, 10, "Table of Contents", ln=1)

            # Reset font to default
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color

            # Add the content for Table of Contents
            toc_content = [
                "Executive Summary ............................................................................................................................... 3",
                "1 Engagement Summary.......................................................................................................... 4",
                "    1.1 Scope.......................................................................................................................................... 4",
                "    1.2 Risk Ratings.................................................................................................................................... 4",
                "    1.3 Findings Overview.................................................................................................................................. 5",
                "2 Technical Details................................................................................................................................... 6",
                "    2.1 SQL Injection ................................................................................................................................... 6",
                "    2.2 Cross-site Request Forgery ........................................................................... 7",
                "    2.3 Information Disclosure ................................................................................................................................. 8"
            ]

            # Add the Table of Contents to the PDF
            for content in toc_content:
                pdf.ln(3)
                pdf.multi_cell(0, 5, content, align="L")
                
                
            sections = [
    ("Confidentiality", ["This document contains sensitive and confidential information, it should not be shared with any other 3rd parties without written permission."]),
    ("GDPR", ["This document may contain personal data subject to the General Data Protection Regulation (GDPR). Handle any personal data in accordance with applicable data protection laws."]),
    ("Disclaimers", ["The information provided in this document is for general informational purposes only and should not be construed as professional advice. The author(s) disclaim any liability for damages arising from the use of this information."]),
    ("Change", ["The author(s) reserve the right to modify these terms. Review this document periodically for updates."]),
    ("Contact", ["For inquiries, contact 087524805"])
]

            # Add text after Table of Contents
            pdf.add_page()
            
            pdf.ln(20)
            pdf.set_font("Arial", "B", 16)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "Legal", ln=1)
            
            # Loop through each section
            for heading, detail in sections:
                # Set font for heading
                pdf.set_font("Arial", "B", 12)
                pdf.set_text_color(255, 0, 0)  # Red color

                # Add heading text
                pdf.cell(0, 10, heading, ln=1)
                

                # Reset font to default
                pdf.set_font("Arial", "", 9)
                pdf.set_text_color(0, 0, 0)  # Reset color

                # Add content for the section
                for paragraph in detail:
                    pdf.multi_cell(0, 5, paragraph, align="L")  
                    pdf.ln(3)  
                        
            
            pdf.set_left_margin(20)
            pdf.set_right_margin(20) 
            
            
            pdf.ln(10)
            
            
            # Change Log
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "Change Log", ln=1)
            pdf.ln(5)  # Add space
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color

            # Define the table headers and data
            headers = ["Date", "Version", "Comments"]
            data = [
                ["1/1/2021", "0.1", "Initial Report"],
                ["10/1/2021", "0.2", "Recon Stage"]
            ]

            # Calculate column widths based on available width
            available_width = pdf.w - pdf.l_margin - pdf.r_margin
            col_widths = [available_width / len(headers)] * len(headers)

            # Add table headers
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            for header, width in zip(headers, col_widths):
                pdf.cell(width, 10, header, border=1, align="C")
            pdf.ln()

            # Add table data
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color
            for row in data:
                for cell, width in zip(row, col_widths):
                    pdf.cell(width, 10, cell, border=1, align="C")
                pdf.ln()

            
            # Add text after images
            pdf.add_page()
            pdf.ln(20)

            # Set font to bold and red
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color

            # Add "Executive Summary" text
            pdf.cell(0, 10, "Executive Summary", ln=1)
            pdf.ln(5)
            # Reset font to default
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color

            # Add the rest of the text
            pdf.multi_cell(0, 5, "CSTAD engaged CYBER-STAD to conduct a security assessment and penetration testing against a website. The main goal of the engagement was to evaluate the security of the platform and identify possible threats and vulnerabilities. This report details the scope of the engagement, detailed information about all of the findings and some recommendations. The summary below is intended for non-technical audiences to give an idea of the overall results of the engagement and the key findings. The second section of this report is intended for a technical audience as it lists all of our findings in detail, along with reproduction steps, analysis, and recommendations. Based on the security assessment we carried for [platform] and based on our findings, the current risk rating is high. The vulnerabilities discovered can be used by malicious actors to cause breaches and even gain unauthorized access to some management pages. The methodology followed is detailed in the following diagram:", align="L")
            
            pdf.image(str(self.output_path / diagram_file), x=None, y=None, w=pdf.w - 20, h=0)
            
            
            
            # -------------------------------pie chart start--------------------------------------------
            # Add section for pie chart
            pdf.add_page()
            pdf.ln(10)
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 10, "The following charts summarize the findings grouped by severity of the threat:", ln=1, align="L")
            pdf.set_font("Arial", "B", 12)
            pdf.ln(10)
            pdf.cell(0, 5, "Vulnerabilities Breakdown", ln=1, align="C")

            # Static data for vulnerabilities breakdown 
            #Dictionary OF vulnerabilities_data DATA NEEDED
            vulnerabilities_data = {             
                'Low': 15,
                'Medium': 30,                
                'High': 20,
                'Critical': 10
            }

            # Generate pie chart
            chart_width = 640
            chart_height = 480
            chart_data = list(vulnerabilities_data.values())
            chart_labels = list(vulnerabilities_data.keys())
            chart_colors = ['#00FF00', '#FFFF00', '#FFA500', '#FF0000']  # Green, Yellow, Orange, Red

            # Create BytesIO object to store the image
            pie_chart_buffer = BytesIO()

            # Generate and save the pie chart
            fig = px.pie(values=chart_data, names=chart_labels, color_discrete_sequence=chart_colors)
            fig.update_layout(width=chart_width, height=chart_height)
            fig.write_image(pie_chart_buffer, format='png')

            # Reset the buffer position to the beginning
            pie_chart_buffer.seek(0)

            # Convert the pie chart image to base64
            chart_base64 = base64.b64encode(pie_chart_buffer.read()).decode('utf-8')

            # Save the pie chart image to a file
            chart_image_path = self.output_path / "pie_chart.png"
            with open(chart_image_path, 'wb') as chart_image_file:
                chart_image_file.write(base64.b64decode(chart_base64))
                
            
            # Embed the pie chart image in the PDF with border 
            
            pdf.image(str(chart_image_path), x=None, y=None, w=pdf.w * 0.7, h=0, type='PNG', link=str(chart_image_path))
           
            # Set the position for the border of pie charts
            border_x1 = 30
            border_y1 = 34
            border_width1 = pdf.w * 0.7
            border_height1 = 108
            # Set the border color and weight
            pdf.set_draw_color(0, 255, 0)  # Red color 
            pdf.set_line_width(1)  # 2px border weight

            
            # Draw the border around the pie chart image
            pdf.rect(border_x1, border_y1, border_width1, border_height1)

            # -----------------------------------pie chart end----------------------------------------
            
            
                
            # bar chart ---------------start------------------------
            
            # Add section for bar chart (Severity Chart)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 5, "Severity Breakdown", ln=1, align="C")

            # Static data for severity breakdown 
            severity_data = {               #Dictionary OF severity_data DATA NEEDED 
                'Low': 5,
                'Medium': 10,
                'High': 8,
                'Critical': 2
            }
            
            
            # Generate bar chart
            bar_chart_width = 640
            bar_chart_height = 480
            bar_chart_data = list(severity_data.values())
            bar_chart_labels = list(severity_data.keys())
            bar_chart_colors = ['#00FF00', '#FFFF00', '#FFA500', '#FF0000']  # Green, Yellow, Orange, Red

            # Create BytesIO object to store the image
            bar_chart_buffer = BytesIO()

            # Generate and save the bar chart
            bar_fig = px.bar(x=bar_chart_labels, y=bar_chart_data, color=bar_chart_labels, color_discrete_sequence=bar_chart_colors)
            bar_fig.update_layout(width=bar_chart_width, height=bar_chart_height)
            bar_fig.write_image(bar_chart_buffer, format='png')

            # Reset the buffer position to the beginning
            bar_chart_buffer.seek(0)

            # Convert the bar chart image to base64
            bar_chart_base64 = base64.b64encode(bar_chart_buffer.read()).decode('utf-8')

            # Embed the bar chart in the PDF
            # Save the bar chart image to a file
            bar_chart_image_path = self.output_path / "bar_chart.png"
            with open(bar_chart_image_path, 'wb') as bar_chart_image_file:
                bar_chart_image_file.write(base64.b64decode(bar_chart_base64))

            
            pdf.set_left_margin(30) 
            # Embed the bar chart image in the PDF with border
            pdf.image(str(bar_chart_image_path), x=None, y=None, w=pdf.w * 0.7, h=0, type='PNG', link=str(bar_chart_image_path))

            # Set the position for the border of bar chart image
            border_x = 30
            border_y = 150
            border_width = pdf.w * 0.7
            border_height = pdf.h * 0.4  # Adjust this fraction

            # Set the border color and weight for the border of bar chart image
            pdf.set_draw_color(255, 182, 193)  # pink color
            pdf.set_line_width(1)  # 2px border weight

            
            # Draw the border around the bar chart image
            pdf.rect(border_x, border_y, border_width, border_height)
            
            #-------------------------------end---------------------------------

            
            
            # Add Engagement Summary section
            pdf.add_page()
            pdf.set_left_margin(20)
            pdf.set_right_margin(20)
            pdf.ln(20)
            pdf.set_font("Arial", "B", 14)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "1 Engagement Summary", ln=1) 
            
            # Add 1.1 Scope subsection
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            # pdf.cell(10)  # Add some indentation
            pdf.cell(0, 10, "1.1 Scope", ln=1)
            
            # Add content for 1.1 Scope 
            scope_content = [                    #LIST OF SCOPE_CONTENT DATA NEEDED 
                "IP",
                "Domain.com",
                "Subdomain.domain.com",
                "Subdomain2.domain.com",
                "...etc"
            ]

            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color
            pdf.cell(0, 10, "As requested, the security assessment was only carried out on the following targets:", ln=1) 


            # Add the content as a list
            for item in scope_content:
                pdf.cell(10)  # Add some indentation
                pdf.cell(0, 5, item, ln=1)
            
            pdf.ln(5)
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "1.2 Risk Ratings", ln=1)   
            
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color
            pdf.multi_cell(0, 5, "The vulnerability risk was calculated based on the Common Vulnerability Scoring System (CVSS v3.0) which is the industry standard for assessing the severity of security vulnerabilities.") 
            pdf.multi_cell(0, 5, "The table below gives a key to the risk naming and colours used throughout this report to provide a clear and  concise risk scoring system. ") 
            
           
            pdf.set_draw_color(0, 0, 0)  
            pdf.set_line_width(0)  
            
            # Risk table
            pdf.ln(5)  # Add space
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)

            # Define the table headers and data
            headers_risk = ["Risk", "CVSS v3.0 Score", "Recommendation"]
            data_risk = [
                ["None", "0.0", " N/A"],
                ["Low", "0.1 - 3.9", "Fix at the next update cycle."],
                ["Medium", "4.0 - 6.9", "Fix immediately if there are 0 high risk vulnerabilities."],
                ["High", "7.0 - 8.9", "Fix immediately if there are 0 critical vulnerabilities."],
                ["Critical", "9.0 - 10.0", "Fix immediately."]
            ]

            # Calculate column widths based on the longest string in each column
            col_widths_risk = [pdf.get_string_width(max(column, key=len)) + 25 for column in zip(*data_risk)]

            # Add table headers
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            for header_risk, width in zip(headers_risk, col_widths_risk):
                pdf.cell(width, 10, header_risk, border=1, align="C")
            pdf.ln()

            # Add table data
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color
            for row_risk in data_risk:
                for cell_risk, width in zip(row_risk, col_widths_risk):
                    pdf.cell(width, 10, cell_risk, border=1)
                pdf.ln()
                
            
            
            # 1.3 finding overview
            pdf.add_page()
            pdf.set_left_margin(20)
            pdf.set_right_margin(20)
            pdf.ln(10)
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "1.3 Findings Overview", ln=1)   
            pdf.ln(5)
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Reset color
            pdf.multi_cell(0, 5, "Below is a list of all the issues found during the engagement along with a brief description, its impact and the risk rating associated with it. Please refer to the 'Risk Ratings' section for more information on how this is calculated.") 
            
            pdf.ln(5)

            # Define the get_background_color function
            def get_background_color(risk_level):
                risk_level_lower = risk_level.lower()
                if "critical" in risk_level_lower:
                    return 255, 0, 0  # Red
                elif "medium" in risk_level_lower:
                    return 255, 165, 0  # Orange
                elif "hard" in risk_level_lower:
                    return 255, 255, 0  # Yellow
                elif "low" in risk_level_lower:
                    return 0, 255, 0  # Green
                else:
                    return 255, 255, 255  # White
                
    
            # Define the table headers and data for the new table
            pdf.ln(5)
            headers_findings = ["ID", "Risk", "Description"] #List of headers_findings are needed
            #List of data_findings are needed too
            data_findings = [
                ["1", "Hard", "SQL Injection leading to unauthorized database access."],
                ["2", "medium", "CSRF - Clients can be forced to submit certain non-critical requests."],
                ["3", "low", "PHP version disclosure - Can help develop attacks for this specific version."]
            ]

            # Calculate column widths based on the longest string in each column
            col_widths_findings = [pdf.get_string_width(max(column, key=len)) + 17 for column in zip(*data_findings)]

            # Add table headers
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(255, 0, 0)  # Red color
            for header_findings, width in zip(headers_findings, col_widths_findings):
                pdf.cell(width, 10, header_findings, border=1, align="C")
            pdf.ln()
            
            # Add table data with dynamic background color
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Red color
            for row_findings in data_findings:
                for index, (cell_findings, width) in enumerate(zip(row_findings, col_widths_findings)):
                    if headers_findings[index] == "Risk":
                        # Get dynamic background color based on risk level
                        background_color = get_background_color(row_findings[1])  # Use the content of the "Risk" cell
                        pdf.set_fill_color(*background_color)
                    else:
                        # Default white background for other cells
                        pdf.set_fill_color(255, 255, 255)
                        
                    pdf.cell(width, 10, cell_findings, border=1, fill=True)
                pdf.ln()
            
            
            
            # Add 2 Technical Details section title
            pdf.add_page()
            pdf.ln(10)
            pdf.set_font("Arial", "B", 14)
            pdf.set_text_color(255, 0, 0)  # Red color
            pdf.cell(0, 10, "2 Technical Details", ln=True)
            pdf.ln(5)
            # Add vulnerability details to the report as a table
          
            pdf.set_font("Arial", "B", 12)  # Set the font to bold, size 14
            pdf.cell(0, 5, "2.1 SQL Injection    CRITICAL      ID: 1", ln=True)
            pdf.ln(3)

            # Set the font to bold, size 9, and red color for the description
            pdf.set_font("Arial", "", 9)
            pdf.set_text_color(0, 0, 0)  # Red color
            pdf.multi_cell(0, 5, "We discovered that using specially crafted requests a malicious actor can communicate with the database and query it to retrieve stored data including data stored in the users tables.")
            pdf.ln()

            # Define the table data for vulnerability details
            data_vulnerability = [
                ["URL", "https://domain.com/news/post.php"],
                ["Parameter", "id"],
                ["References", "https://owasp.org/www-community/attacks/SQL_Injection"],
                ["Request", "POST /news/post.php HTTP/1.1\nHost: domain.com\nAccept: application/json, text/plain, */*"],
                ["Response", "HTTP/1.1 200 OK\nContent-Type: application/json; charset=utf-8\nVary: Accept-Encoding"]
                # Add more details as needed
            ]

            # Calculate column widths based on the longest string in each column
            col_widths_vulnerability = [pdf.get_string_width(max(column, key=len)) + 15 for column in zip(*data_vulnerability)]

            # Add table data with bold headers
            pdf.set_font("Arial", "B", 9)  # Set the font to bold for headers
            for row_vulnerability in data_vulnerability:
                for index, (cell_vulnerability, width) in enumerate(zip(row_vulnerability, col_widths_vulnerability)):
                    if index == 0:  # Bold only the first cell (header)
                        pdf.set_font("Arial", "B", 9)
                    else:
                        pdf.set_font("Arial", "", 9)

                    pdf.cell(width, 10, cell_vulnerability, border=1)
                pdf.ln()

            # Set the font back to regular
            pdf.set_font("Arial", "", 9)

                
            pdf.output(str(self.output_path / file_name), "F")
            print(f"----> File Pentest Report ---- '{file_name}' ----- generated successfully.")

# Call func
report = Report()
report.generate_report()

