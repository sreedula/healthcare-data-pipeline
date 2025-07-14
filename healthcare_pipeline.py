"""
Healthcare Data Pipeline Starter Project
========================================

This template provides the structure for your healthcare data processing system.
Complete the TODO sections to build a working care gap identification system.

Author: [Your Name]
Date: [Current Date]
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class HealthcareDataProcessor:
    """
    Main class for processing healthcare data and identifying care gaps.
    """
    
    def __init__(self):
        """Initialize the processor with empty data containers."""
        self.patients_df = None
        self.visits_df = None
        self.screening_df = None
        self.lab_results_df = None
        self.care_gaps = []
        self.data_quality_issues = []
    
    def load_data(self):
        """
        Load all CSV files into pandas DataFrames.
        
        Files to load:
        - patients.csv
        - visits.csv  
        - screening_due.csv
        - lab_results.csv
        """
        print("Loading healthcare data files...")
        
        try:
            # TODO: Load patients.csv into self.patients_df
            # Hint: Use pd.read_csv() function
            self.patients_df = pd.read_csv('patients.csv')
            
            # TODO: Load visits.csv into self.visits_df
            self.visits_df = pd.read_csv('visits.csv')
            
            # TODO: Load screening_due.csv into self.screening_df
            self.screening_df = pd.read_csv('screenings.csv')
            
            # TODO: Load lab_results.csv into self.lab_results_df
            self.lab_results_df = pd.read_csv('lab_results.csv')
            
            print("✓ All data files loaded successfully!")
            
        except FileNotFoundError as e:
            print(f"❌ Error loading file: {e}")
            print("Make sure all CSV files are in the same directory as this script.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def explore_data(self):
        """
        Display basic information about the loaded datasets.
        Show record counts, column names, and sample data.
        """
        print("\n" + "="*50)
        print("DATA EXPLORATION SUMMARY")
        print("="*50)
        
        # TODO: Print the number of patients
        # Hint: Use len(self.patients_df) if data is loaded
        print(f"Number of patients: {len(self.patients_df)}")
        
        # TODO: Print the number of visits
        print(f"Number of visits: {len(self.visits_df)}")
        
        # TODO: Print the number of screening records
        print(f"Number of screening records: {len(self.screening_df)}")
        
        # TODO: Print the number of lab results
        print(f"Number of lab results: {len(self.lab_results_df)}")
        
        print("\nPatients Dataset:")
        # TODO: Display first 3 rows of patients data
        # Hint: Use self.patients_df.head(3)
        print(self.patients_df.head(3))
        
        print("\nColumn names in patients dataset:")
        # TODO: Print list of column names
        # Hint: Use list(self.patients_df.columns)
        print(list(self.patients_df.columns))
        
        # TODO: Show basic statistics for patient ages
        # Hint: Use self.patients_df['age'].describe()
        print("\nAge Statistics:")
        print(self.patients_df['age'].describe())
        
        # Show gender breakdown
        print("\nGender Breakdown:")
        print(self.patients_df['gender'].value_counts())
        
        # Show unique diagnoses
        print("\nUnique Diagnoses:")
        print(self.patients_df['primary_diagnosis'].unique())
        
    def clean_data(self):
        """
        Clean and standardize the data.
        Remove duplicates, fix formatting, handle missing values.
        """
        print("\n" + "="*50)
        print("CLEANING DATA")
        print("="*50)
        
        original_count = len(self.patients_df)
        
        # TODO: Remove duplicate patients based on patient_id
        # Hint: Use drop_duplicates() method
        self.patients_df = self.patients_df.drop_duplicates(subset=['patient_id'])
        
        after_dedup_count = len(self.patients_df)
        duplicates_removed = original_count - after_dedup_count
        print(f"Removed {duplicates_removed} duplicate patient records")
        
        # TODO: Standardize gender codes to 'M' and 'F'
        # Hint: Use str.upper() method
        self.patients_df['gender'] = self.patients_df['gender'].str.upper()
        
        # TODO: Convert date columns to datetime format
        # For visits_df: convert 'visit_date' and 'next_appointment' columns
        # For screening_df: convert all date columns (they end with '_due')
        # Hint: Use pd.to_datetime() with errors='coerce' to handle invalid dates
        if 'visit_date' in self.visits_df.columns:
            self.visits_df['visit_date'] = pd.to_datetime(self.visits_df['visit_date'], errors='coerce')
        if 'next_appointment' in self.visits_df.columns:
            self.visits_df['next_appointment'] = pd.to_datetime(self.visits_df['next_appointment'], errors='coerce')
        
        date_columns = [col for col in self.screening_df.columns if col.endswith('_due')]
        for col in date_columns:
            self.screening_df[col] = pd.to_datetime(self.screening_df[col], errors='coerce')
        
        print("✓ Data cleaning completed!")
    
    def validate_data_quality(self):
        """
        Check for data quality issues and report them.
        """
        print("\n" + "="*50)
        print("DATA QUALITY VALIDATION")
        print("="*50)
        
        self.data_quality_issues = []
        
        # TODO: Check for missing patient IDs
        # If any patient_id is null, add issue to self.data_quality_issues list
        missing_patient_ids = self.patients_df['patient_id'].isnull().sum()
        if missing_patient_ids > 0:
            self.data_quality_issues.append(f"Missing patient IDs: {missing_patient_ids}")
        
        # TODO: Check for invalid ages (negative or > 120)
        # Count how many patients have invalid ages
        invalid_ages = len(self.patients_df[(self.patients_df['age'] < 0) | (self.patients_df['age'] > 120)])
        if invalid_ages > 0:
            self.data_quality_issues.append(f"Invalid ages (negative or >120): {invalid_ages}")
        
        # TODO: Check for invalid gender codes (not M or F)
        # Count how many patients have invalid gender
        invalid_gender = len(self.patients_df[~self.patients_df['gender'].isin(['M', 'F'])])
        if invalid_gender > 0:
            self.data_quality_issues.append(f"Invalid gender codes: {invalid_gender}")
        
        # TODO: Check for missing phone numbers or email addresses
        missing_phone = self.patients_df['phone'].isnull().sum()
        missing_email = self.patients_df['email'].isnull().sum()
        if missing_phone > 0:
            self.data_quality_issues.append(f"Missing phone numbers: {missing_phone}")
        if missing_email > 0:
            self.data_quality_issues.append(f"Missing email addresses: {missing_email}")
        
        # TODO: Print summary of data quality issues found
        if self.data_quality_issues:
            print("⚠️  Data Quality Issues Found:")
            for issue in self.data_quality_issues:
                print(f"   - {issue}")
        else:
            print("✓ No data quality issues found!")
    
    def calculate_patient_ages(self):
        """
        Calculate or verify patient ages.
        This is a helper function for age-based screening rules.
        """
        # TODO: If you want, add logic to calculate ages from birth dates
        # For now, we'll use the age column as provided
        # In a real system, you might calculate ages from birth dates
        pass
    
    def identify_care_gaps(self):
        """
        Identify patients who need preventive care based on screening guidelines.
        
        Screening Rules:
        - Mammograms: Women 40+ years old
        - Colonoscopies: Everyone 50+ years old  
        - Annual visits: Everyone (within last 12 months)
        - Flu shots: Everyone (annually by October 1st)
        """
        print("\n" + "="*50)
        print("IDENTIFYING CARE GAPS")
        print("="*50)
        
        today = datetime.now()
        self.care_gaps = []
        
        # Merge patients with screening data for easier processing
        merged_data = self.patients_df.merge(self.screening_df, on='patient_id', how='left')
        
        # TODO: Loop through each patient and check for care gaps
        for index, patient in merged_data.iterrows():
            patient_gaps = []
            
            # TODO: Check if patient needs mammogram
            # Rule: Women (gender == 'F') aged 40 or older
            # Check if mammogram_due date has passed or is missing
            if patient['gender'] == 'F' and patient['age'] >= 40:
                mammogram_due = patient.get('mammogram_due')
                if pd.isna(mammogram_due) or mammogram_due < today:
                    patient_gaps.append('Mammogram overdue')
            
            # TODO: Check if patient needs colonoscopy
            # Rule: Everyone aged 50 or older
            # Check if colonoscopy_due date has passed or is missing
            if patient['age'] >= 50:
                colonoscopy_due = patient.get('colonoscopy_due')
                if pd.isna(colonoscopy_due) or colonoscopy_due < today:
                    patient_gaps.append('Colonoscopy overdue')
            
            # TODO: Check if patient needs annual visit
            # Rule: Everyone should have visited within last 12 months
            # Compare last visit date with current date
            patient_visits = self.visits_df[self.visits_df['patient_id'] == patient['patient_id']]
            if len(patient_visits) > 0:
                last_visit = patient_visits['visit_date'].max()
                if pd.isna(last_visit) or (today - last_visit).days > 365:
                    patient_gaps.append('Annual visit overdue')
            else:
                patient_gaps.append('Annual visit overdue')
            
            # TODO: Check if patient needs flu shot
            # Rule: Everyone should get flu shot by October 1st each year
            # Check if flu_shot_due date has passed
            flu_shot_due = patient.get('flu_shot_due')
            if pd.isna(flu_shot_due) or flu_shot_due < today:
                patient_gaps.append('Flu shot needed')
            
            # If any gaps found, add patient to care_gaps list
            if patient_gaps:
                self.care_gaps.append({
                    'patient_id': patient['patient_id'],
                    'name': f"{patient['first_name']} {patient['last_name']}",
                    'age': patient['age'],
                    'gender': patient['gender'],
                    'phone': patient['phone'],
                    'email': patient['email'],
                    'gaps': patient_gaps,
                    'priority': self._calculate_priority(patient_gaps, patient)
                })
        
        print(f"✓ Identified {len(self.care_gaps)} patients with care gaps")
    
    def _calculate_priority(self, gaps, patient):
        """
        Calculate priority level based on gap types and patient factors.
        This is a helper function for the care gap identification.
        """
        today = datetime.now()
        priority_score = 0
        
        for gap in gaps:
            if 'overdue' in gap.lower():
                priority_score += 2
            elif 'needed' in gap.lower():
                priority_score += 1
            
            # Higher priority for older patients
            if patient['age'] >= 65:
                priority_score += 1
        
        if priority_score >= 3:
            return 'High'
        elif priority_score >= 2:
            return 'Medium'
        else:
            return 'Low'
    
    def categorize_gaps_by_priority(self):
        """
        Categorize care gaps by priority level and type.
        """
        print("\n" + "="*50)
        print("CATEGORIZING CARE GAPS")
        print("="*50)
        
        gap_types = {}
        priority_counts = {'High': 0, 'Medium': 0, 'Low': 0}
        
        for patient in self.care_gaps:
            # Count by priority
            priority_counts[patient['priority']] += 1
            
            # Count by gap type
            for gap in patient['gaps']:
                if gap not in gap_types:
                    gap_types[gap] = 0
                gap_types[gap] += 1
        
        print("Gap Types:")
        for gap_type, count in gap_types.items():
            print(f"  - {gap_type}: {count} patients")
        
        print("\nPriority Levels:")
        for priority, count in priority_counts.items():
            print(f"  - {priority} Priority: {count} patients")
        
        return gap_types, priority_counts
    
    def generate_summary_report(self):
        """
        Generate a comprehensive summary report.
        """
        print("\n" + "="*50)
        print("GENERATING SUMMARY REPORT")
        print("="*50)
        
        total_patients = len(self.patients_df)
        patients_with_gaps = len(self.care_gaps)
        gap_percentage = (patients_with_gaps / total_patients) * 100 if total_patients > 0 else 0
        
        gap_types, priority_counts = self.categorize_gaps_by_priority()
        
        # Generate report text
        report = f"""=== CARE GAP REPORT ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Total Patients: {total_patients}
Patients with Care Gaps: {patients_with_gaps} ({gap_percentage:.1f}%)

Gap Types:"""
        
        for gap_type, count in gap_types.items():
            report += f"\n- {gap_type}: {count} patients"
        
        report += f"""

Priority Levels:
- High Priority: {priority_counts['High']} patients
- Medium Priority: {priority_counts['Medium']} patients  
- Low Priority: {priority_counts['Low']} patients

Data Quality Issues: {len(self.data_quality_issues)} found
"""
        
        print(report)
        
        # Save report to file
        with open('summary_statistics.txt', 'w') as f:
            f.write(report)
        
        print("✓ Summary report saved to 'summary_statistics.txt'")
        
        return report
    
    def create_visualizations(self):
        """
        Create charts and graphs to visualize the care gap data.
        """
        print("\n" + "="*50)
        print("CREATING VISUALIZATIONS")
        print("="*50)
        
        if not self.care_gaps:
            print("No care gaps to visualize!")
            return
        
        # Create figure with subplots for multiple charts
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Healthcare Care Gap Analysis', fontsize=16)
        
        # 1. Gap types bar chart
        gap_types, _ = self.categorize_gaps_by_priority()
        ax1.bar(gap_types.keys(), gap_types.values(), color='skyblue')
        ax1.set_title('Care Gaps by Type')
        ax1.set_ylabel('Number of Patients')
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. Priority levels pie chart
        _, priority_counts = self.categorize_gaps_by_priority()
        if sum(priority_counts.values()) > 0:
            ax2.pie(priority_counts.values(), labels=priority_counts.keys(), autopct='%1.1f%%')
            ax2.set_title('Care Gaps by Priority Level')
        
        # 3. Age distribution of patients with gaps
        ages = [patient['age'] for patient in self.care_gaps]
        ax3.hist(ages, bins=10, color='lightgreen', alpha=0.7)
        ax3.set_title('Age Distribution of Patients with Care Gaps')
        ax3.set_xlabel('Age')
        ax3.set_ylabel('Number of Patients')
        
        # 4. Gender breakdown of patients with gaps
        gender_counts = {}
        for patient in self.care_gaps:
            gender = patient['gender']
            gender_counts[gender] = gender_counts.get(gender, 0) + 1
        
        if gender_counts:
            ax4.bar(gender_counts.keys(), gender_counts.values(), color='orange')
            ax4.set_title('Care Gaps by Gender')
            ax4.set_ylabel('Number of Patients')
        
        plt.tight_layout()
        plt.savefig('care_gaps_chart.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✓ Visualization saved as 'care_gaps_chart.png'")
    
    def export_results(self):
        """
        Export detailed results to CSV files.
        """
        print("\n" + "="*50)
        print("EXPORTING RESULTS")
        print("="*50)
        
        if self.care_gaps:
            # Create detailed care gaps report
            gaps_data = []
            for patient in self.care_gaps:
                gaps_data.append({
                    'patient_id': patient['patient_id'],
                    'name': patient['name'],
                    'age': patient['age'],
                    'gender': patient['gender'],
                    'phone': patient['phone'],
                    'email': patient['email'],
                    'care_gaps': ', '.join(patient['gaps']),
                    'priority': patient['priority']
                })
            
            gaps_df = pd.DataFrame(gaps_data)
            gaps_df.to_csv('care_gaps_report.csv', index=False)
            print("✓ Care gaps report saved to 'care_gaps_report.csv'")
        
        # Create data quality report
        if self.data_quality_issues:
            with open('data_quality_report.txt', 'w') as f:
                f.write("=== DATA QUALITY REPORT ===\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("Issues Found:\n")
                for issue in self.data_quality_issues:
                    f.write(f"- {issue}\n")
            print("✓ Data quality report saved to 'data_quality_report.txt'")
    
    def run_full_analysis(self):
        """
        Run the complete healthcare data analysis pipeline.
        This is the main function that calls all other methods in order.
        """
        print("🏥 Healthcare Data Pipeline Starting...")
        print("=" * 60)
        
        # Step 1: Load data
        self.load_data()
        
        # Step 2: Explore data
        self.explore_data()
        
        # Step 3: Clean data
        self.clean_data()
        
        # Step 4: Validate data quality
        self.validate_data_quality()
        
        # Step 5: Identify care gaps
        self.identify_care_gaps()
        
        # Step 6: Generate reports
        self.generate_summary_report()
        
        # Step 7: Create visualizations
        self.create_visualizations()
        
        # Step 8: Export results
        self.export_results()
        
        print("\n" + "="*60)
        print("🎉 Analysis completed successfully!")
        print("Check the generated files for detailed results.")
        print("="*60)


def main():
    """
    Main function to run the healthcare data analysis.
    """
    # TODO: Create an instance of HealthcareDataProcessor
    processor = HealthcareDataProcessor()
    
    # TODO: Run the full analysis
    processor.run_full_analysis()
    
    print("\nThank you for using the Healthcare Data Pipeline!")


# Helper functions (optional - implement if needed)
def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.
    Useful for determining how overdue a screening is.
    """
    # TODO: Implement if you want to calculate priority levels
    if pd.isna(date1) or pd.isna(date2):
        return None
    return (date2 - date1).days


def format_phone_number(phone):
    """
    Standardize phone number format.
    """
    # TODO: Implement if you want to clean phone numbers
    if pd.isna(phone):
        return None
    # Remove all non-digit characters
    digits = ''.join(filter(str.isdigit, str(phone)))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone


def validate_email(email):
    """
    Check if email address is valid format.
    """
    # TODO: Implement if you want to validate email addresses
    if pd.isna(email):
        return False
    return '@' in str(email) and '.' in str(email)


# Run the program
if __name__ == "__main__":
    main()