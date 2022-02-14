# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program

def print_good_cholostorol():
    # good level
    print('*** Good level of cholestrol ***')

def print_high_cholostorol():
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')

def print_TLC_diet():
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')

def check_cholostrol(total_cholostrol, ldl, triglyceride):

    if total_cholostrol < 200 and ldl < 100 and triglyceride < 150:
        return print_good_cholostorol()
    elif 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200:
        return print_high_cholostorol()
    elif 200 <total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200:
        return print_TLC_diet()
    else:
        return print('Error: unhandled case.')

check_cholostrol(70, 30, 120)