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
            
            # TODO: Load visits.csv into self.visits_df
            
            # TODO: Load screening_due.csv into self.screening_df
            
            # TODO: Load lab_results.csv into self.lab_results_df
            
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
        
        # TODO: Print the number of visits
        
        # TODO: Print the number of screening records
        
        # TODO: Print the number of lab results
        
        print("\nPatients Dataset:")
        # TODO: Display first 3 rows of patients data
        # Hint: Use self.patients_df.head(3)
        
        print("\nColumn names in patients dataset:")
        # TODO: Print list of column names
        # Hint: Use list(self.patients_df.columns)
        
        # TODO: Show basic statistics for patient ages
        # Hint: Use self.patients_df['age'].describe()
        
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
        
        after_dedup_count = len(self.patients_df)
        duplicates_removed = original_count - after_dedup_count
        print(f"Removed {duplicates_removed} duplicate patient records")
        
        # TODO: Standardize gender codes to 'M' and 'F'
        # Hint: Use str.upper() method
        
        # TODO: Convert date columns to datetime format
        # For visits_df: convert 'visit_date' and 'next_appointment' columns
        # For screening_df: convert all date columns (they end with '_due')
        # Hint: Use pd.to_datetime() with errors='coerce' to handle invalid dates
        
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
        
        # TODO: Check for invalid ages (negative or > 120)
        # Count how many patients have invalid ages
        
        # TODO: Check for invalid gender codes (not M or F)
        # Count how many patients have invalid gender
        
        # TODO: Check for missing phone numbers or email addresses
        
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
        
        # TODO: Loop through each patient and check for care gaps
        for index, patient in self.patients_df.iterrows():
            patient_gaps = []
            
            # TODO: Check if patient needs mammogram
            # Rule: Women (gender == 'F') aged 40 or older
            # Check if mammogram_due date has passed or is missing
            
            # TODO: Check if patient needs colonoscopy
            # Rule: Everyone aged 50 or older
            # Check if colonoscopy_due date has passed or is missing
            
            # TODO: Check if patient needs annual visit
            # Rule: Everyone should have visited within last 12 months
            # Compare last visit date with current date
            
            # TODO: Check if patient needs flu shot
            # Rule: Everyone should get flu shot by October 1st each year
            # Check if flu_shot_due date has passed
            
            # If any gaps found, add patient to care_gaps list
            if patient_gaps:
                self.care_gaps.append({
                    'patient_id': patient['patient_id'],
                    'name': f"{patient['first_name']} {patient['last_name']}",
                    'age': patient['age'],
                    'gender': patient['gender'],
                    'phone': patient['phone'],
                    'gaps': patient_gaps
                })
        
        print(f"✓ Care gap analysis completed!")
        print(f"Found {len(self.care_gaps)} patients with care gaps")
    
    def categorize_gaps_by_priority(self):
        """
        Categorize care gaps by priority level based on how overdue they are.
        
        Priority Levels:
        - High: Overdue by > 6 months
        - Medium: Due within next 30 days  
        - Low: Due within next 3 months
        """
        # TODO: Add priority levels to care gaps
        # This is an optional enhancement - implement if time allows
        pass
    
    def generate_summary_report(self):
        """
        Generate and display a summary report of care gaps.
        """
        print("\n" + "="*60)
        print("CARE GAP SUMMARY REPORT")
        print("="*60)
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        total_patients = len(self.patients_df)
        patients_with_gaps = len(self.care_gaps)
        
        # TODO: Calculate and display basic statistics
        # - Total number of patients
        # - Number of patients with care gaps
        # - Percentage of patients with care gaps
        
        # TODO: Count different types of care gaps
        # Create a dictionary to count each gap type
        gap_counts = {}
        
        # TODO: Loop through care_gaps and count each gap type
        
        # TODO: Display gap counts
        print("\nCare Gap Breakdown:")
        
        # TODO: Display individual patients with gaps
        print(f"\nPatients Requiring Follow-up:")
        print("-" * 40)
        
    def create_visualizations(self):
        """
        Create charts and graphs to visualize care gap data.
        """
        print("\n" + "="*50)
        print("CREATING VISUALIZATIONS")
        print("="*50)
        
        # TODO: Create a bar chart showing different types of care gaps
        # Count each gap type first
        gap_counts = {}
        for patient in self.care_gaps:
            for gap in patient['gaps']:
                gap_counts[gap] = gap_counts.get(gap, 0) + 1
        
        if gap_counts:
            # TODO: Create bar chart
            # Hint: Use plt.figure(), plt.bar(), plt.title(), plt.show()
            
            # TODO: Save the chart as an image file
            # Hint: Use plt.savefig('care_gaps_chart.png')
            
            print("✓ Care gap visualization created and saved!")
        else:
            print("No care gaps found - no visualization needed.")
    
    def export_results(self):
        """
        Export results to CSV files for use by healthcare staff.
        """
        print("\n" + "="*50)
        print("EXPORTING RESULTS")
        print("="*50)
        
        # TODO: Create a DataFrame with care gap details
        # Include: patient_id, name, age, gender, phone, gap_types
        
        # TODO: Save care gaps to CSV file
        # Hint: Use DataFrame.to_csv('care_gaps_report.csv')
        
        # TODO: Save summary statistics to text file
        
        print("✓ Results exported successfully!")
    
    def run_full_analysis(self):
        """
        Run the complete analysis pipeline.
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
    
    # TODO: Run the full analysis
    
    print("\nThank you for using the Healthcare Data Pipeline!")


# Helper functions (optional - implement if needed)
def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.
    Useful for determining how overdue a screening is.
    """
    # TODO: Implement if you want to calculate priority levels
    pass


def format_phone_number(phone):
    """
    Standardize phone number format.
    """
    # TODO: Implement if you want to clean phone numbers
    pass


def validate_email(email):
    """
    Check if email address is valid format.
    """
    # TODO: Implement if you want to validate email addresses
    pass


# Run the program
if __name__ == "__main__":
    main()