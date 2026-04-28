import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CCRB-Complaint-Data_202007271729/allegations_202007271729.csv')
print(df.head())

print("\n1. DATASET SIZE:")
print(f"   Total rows: {len(df):,}")
print(f"   Total columns: {len(df.columns)}")

print("\n2. ALL COLUMNS:")
for i, col in enumerate(df.columns):
    print(f"   {i+1}. {col}")

print("\n3. BOARD DISPOSITIONS (OUTCOMES):")
disposition_counts = df['board_disposition'].value_counts()
for outcome, count in disposition_counts.items():
    pct = count/len(df)*100
    print(f"   {outcome}: {count:,} ({pct:.1f}%)")

print("\n4. MEANINGFUL DISCIPLINE VS NO DISCIPLINE:")
meaningful = ['Substantiated (Charges)', 'Substantiated (Command Discipline A)']
no_discipline = ['Unsubstantiated', 'Exonerated', 'Unfounded', 'Miscellaneous']

meaningful_count = df[df['board_disposition'].isin(meaningful)].shape[0]
no_discipline_count = df[df['board_disposition'].isin(no_discipline)].shape[0]
other_count = len(df) - meaningful_count - no_discipline_count

print(f"   Meaningful discipline: {meaningful_count:,} ({meaningful_count/len(df)*100:.1f}%)")
print(f"   No discipline: {no_discipline_count:,} ({no_discipline_count/len(df)*100:.1f}%)")
print(f"   Other/Unknown: {other_count:,} ({other_count/len(df)*100:.1f}%)")

print("\n5. PROPOSITION CHECK:")
print(f"   Proposition: 'More than 70% of complaints result in NO disciplinary action'")
print(f"   Actual NO discipline: {no_discipline_count/len(df)*100:.1f}%")
if no_discipline_count/len(df)*100 > 70:
    print("   PROPOSITION SUPPORTED by data - Use earnest techniques for Viz A")
else:
    print("   ⚠️ Proposition NOT supported - You'll need deceptive techniques for Viz A")

if 'unique_mos_id' in df.columns:
    print("\n6. OFFICER COMPLAINT DISTRIBUTION:")
    officer_counts = df['unique_mos_id'].value_counts()
    print(f"   Total unique officers: {len(officer_counts):,}")
    print(f"   Officers with 1 complaint: {(officer_counts == 1).sum():,}")
    print(f"   Officers with 2-5 complaints: {((officer_counts >= 2) & (officer_counts <= 5)).sum():,}")
    print(f"   Officers with 6-10 complaints: {((officer_counts >= 6) & (officer_counts <= 10)).sum():,}")
    print(f"   Officers with 10+ complaints: {(officer_counts > 10).sum():,}")
    print(f"   Officer with most complaints: {officer_counts.max()}")

print("\n7. RACE/ETHNICITY COLUMNS CHECK:")
race_cols = [col for col in df.columns if 'race' in col.lower() or 'ethnic' in col.lower()]
if race_cols:
    print(f"   Found: {race_cols}")
    for col in race_cols:
        print(f"   {col} unique values: {df[col].nunique()}")
 