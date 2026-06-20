import os
import random

# Load image pool (10 CDN images)
pool_path = "landing_pages/github_image_links.txt"
with open(pool_path, "r") as f:
    raw = [line.strip() for line in f if line.strip()]
    # Switch branch from @main to @high-quality-images to match existing pages
    image_pool = [url.replace("@main", "@high-quality-images") for url in raw]

checkout_link = "https://oliviaselfcare.gumroad.com/l/recepies?wanted=true"

# Track used image triplets to avoid repeats
used_triplets = set()

def pick_images():
    for _ in range(200):
        trio = tuple(sorted(random.sample(range(10), 3)))
        if trio not in used_triplets:
            used_triplets.add(trio)
            return [image_pool[i] for i in trio]
    return random.sample(image_pool, 3)

# 70 new unique headlines
new_headlines = [
    # Extending existing themes
    "The 21-Day Clean Eating Challenge: Your Complete Guide to Lasting Health",
    "21 Days to a New You: The Ultimate Clean Eating Transformation Plan",
    "The 21-Day Reset: Jumpstart Your Health with Simple, Delicious Recipes",
    "Clean Eating for Beginners: Your 90-Day Roadmap to Vibrant Health",
    "The Beginner's Guide to Clean Eating: Simple Steps, Big Results",
    "From Zero to Clean Eating Hero: The Ultimate Beginner's Playbook",
    "Boost Your Energy Naturally: The Lazy Cook's Guide to Vitality",
    "End the Afternoon Slump: Energize Your Body with Clean Eating",
    "The Energy-Boosting Meal Plan: Feel Alive with Every Bite",
    "The Easiest Way to Transform Your Diet: Clean Eating Made Simple",
    "Clean Eating on Autopilot: Simple Recipes That Do the Work for You",
    "The No-Effort Clean Eating System: Results Without the Stress",
    "Eat Better Without Trying: The Lazy Person's Guide to Clean Eating",
    "Stress-Free Healthy Eating: How to Eat Well Without Overthinking It",
    "Let Go of Diet Stress: The Peaceful Path to Clean Eating Success",
    "The Anti-Stress Eating Plan: Nourish Your Body, Calm Your Mind",
    "Clean Eating Made Effortless: Simple Recipes for Real Results",
    "The Effortless Clean Eating Blueprint: Maximum Results, Minimum Work",
    "Feel Your Best Every Day: The Complete Clean Eating Wellness Plan",
    "Wake Up Energized: The Clean Eating Plan That Transforms Your Mornings",
    "Look and Feel Amazing: The Summer-Ready Clean Eating Guide",
    "The Year-Round Wellness Plan: Feel Your Best in Every Season",
    "Fuel Your Body for Peak Performance: The Clean Eating Athlete's Guide",
    "The Ultimate Nutrition Fuel-Up: Clean Eating for Active Lifestyles",
    "Food as Fuel: The Practical Guide to Eating for Energy and Focus",
    "Healthy Eating, Finally Made Simple: 75 Recipes for Real Life",
    "The No-Nonsense Guide to Healthy Eating: Cut the Confusion, Keep the Flavor",
    "Real Food, Real Results: The Simplified Path to Healthy Eating",
    "The Lazy Cook's Complete Collection: 125+ Recipes for Effortless Healthy Eating",
    "The Lazy Cook's Meal Prep Bible: Cook Once, Eat Healthy All Week",
    "The Ultimate Lazy Cook's Kitchen Guide: Minimal Effort, Maximum Taste",
    "Your Mid-Year Health Revival: The Complete Reset Plan",
    "Mid-Year Momentum: Reboot Your Eating Habits and Finish Strong",
    "The Summer Reset You Actually Want: Clean Eating Made Fun and Easy",
    "No-Fuss Healthy Eating: The Busy Professional's Guide to Clean Food",
    "Clean Eating for the Chaos of Life: Simple Recipes When You Have No Time",
    "The 15-Minute Meal Solution: Gourmet Clean Eating on a Tight Schedule",
    "Vibrant Health When You're Short on Time: The 20-Minute Meal Plan",
    "Quick, Fresh, and Healthy: The Vibrant Health Express Cookbook",
    "Your Personalized Path to Wellness: A Clean Eating Plan That Fits YOU",
    "The Custom Clean Eating Blueprint: Your Body, Your Rules, Your Success",
    "Simple Success: The No-Overwhelm Clean Eating System That Actually Works",
    "Stop Wasting Time on Complicated Diets: The Simple Success Method",
    # New themes
    "Clean Eating on a Budget: 75 Affordable Recipes for Healthy Living",
    "Eat Healthy Without Breaking the Bank: The Budget-Friendly Clean Eating Guide",
    "The Smart Shopper's Guide to Clean Eating: Delicious Meals for Less",
    "Family-Friendly Clean Eating: Meals the Whole Family Will Love",
    "Feed Your Family Well: The Complete Guide to Healthy Family Meals",
    "The Busy Mom's Clean Eating Survival Guide: Quick Meals, Happy Kids",
    "Breakfast Made Easy: 30 Quick Clean Eating Recipes to Start Your Day Right",
    "The Ultimate Breakfast Revolution: Energizing Clean Meals for Morning People",
    "Lunchtime Solutions: Delicious Clean Eating Meals for Your Workday",
    "Dinner in 20: The Weeknight Clean Eating Solution for Tired Cooks",
    "One-Pot Clean Eating: Minimal Dishes, Maximum Flavor",
    "The One-Pot Wonder: Gourmet Clean Meals with Zero Cleanup",
    "Meal Prep Sunday: Your Weekly Clean Eating Game Plan",
    "The Meal Prep Masters' Guide: Set Yourself Up for a Week of Success",
    "The Clean Eating Snack Bible: 30 Healthy Bites to Keep You on Track",
    "Smart Snacking: How to Stay Full and Focused Between Meals",
    "Sugar Detox Made Simple: Break Free from Cravings in 14 Days",
    "The 14-Day Sugar Detox: Drop the Sugar, Keep the Sweetness",
    "Gluten-Free Clean Eating: Delicious Recipes for a Healthier You",
    "The Plant-Powered Kitchen: Beginner-Friendly Clean Plant-Based Recipes",
    "High-Protein Clean Eating: Build Strength and Stay Satisfied",
    "The Clean Eating Comfort Food Cookbook: Healthy Versions of Your Favorites",
    "Guilt-Free Comfort Food: Healthy Eating That Actually Tastes Indulgent",
    "The Complete Clean Eating Pantry Guide: Stock Your Kitchen for Success",
    "Clean Eating for Weight Loss: Drop Pounds Without Feeling Deprived",
    "The Weight Loss Secret That Works: Clean Eating Made Simple and Sustainable",
    "Transform Your Body in 30 Days: The Ultimate Clean Eating Challenge",
    "The 30-Day Clean Eating Revolution: Your Body Will Thank You",
    "Clean Eating for Gut Health: Heal Your Digestion from the Inside Out",
    "The Gut Health Reset: Restore Your Digestive Health with Clean Food",
    "The Complete Clean Eating Starter Kit: Everything You Need to Begin",
    "Your First Week of Clean Eating: A Step-by-Step Guide for Beginners",
    "The Clean Eating Beginner's Bootcamp: 7 Days to a Healthier Lifestyle",
    "From Cravings to Control: The Complete Guide to Food Freedom",
    "The No-Deprivation Diet: Eat Clean, Indulge Smart, Live Well",
    "Clean Eating for Long-Term Health: Build Habits That Last a Lifetime",
    "The Habit Builder's Guide to Clean Eating: Small Changes, Big Transformations",
    "The Complete Clean Eating Library: Recipes, Plans, and Wisdom for Life",
    "Finally Free from Diet Confusion: The Truth About Clean Eating Revealed",
    "The Ultimate Guide to Eating Clean: No Hype, Just Results",
]

# Ensure we have exactly enough headlines
assert len(new_headlines) >= 70, f"Need 70 headlines, only have {len(new_headlines)}"

# Slugs for new pages - extend existing themes + new themes
slug_groups = [
    # Existing themes extended (need to check last number used)
    ("21-day-clean-eating-challenge", 3, 5),       # -3 through -5
    ("beginners-roadmap-clean-eating", 4, 6),       # -4 through -6
    ("boost-energy-lazy-cook-plan", 4, 6),          # -4 through -6
    ("clean-eating-beginners-75-recipes", 3, 5),    # -3 through -5
    ("easiest-way-clean-eating", 4, 7),             # -4 through -7
    ("eat-better-stress-less", 4, 6),               # -4 through -6
    ("effortless-clean-eating", 3, 4),              # -3 through -4
    ("feel-your-best-summer", 4, 6),                # -4 through -6
    ("fuel-your-body-no-stress", 4, 6),             # -4 through -6
    ("get-your-energy-back", 2, 3),                 # -2 through -3
    ("healthy-eating-simplified", 4, 6),            # -4 through -6
    ("lazy-cook-guide-healthy-eating", 5, 8),       # -5 through -8
    ("mid-year-reset", 4, 5),                       # -4 through -5
    ("no-fuss-healthy-eating", 4, 6),               # -4 through -6
    ("personalized-wellness-journey", 3, 4),        # -3 through -4
    ("simple-way-clean-eating-success", 2, 3),      # -2 through -3
    ("stop-stressing-about-dinner", 2, 3),          # -2 through -3
    ("summer-2026-glow-up", 3, 4),                  # -3 through -4
    ("summer-2026-reset", 3, 4),                    # -3 through -4
    ("transform-lifestyle-21-days", 4, 5),          # -4 through -5
    ("vibrant-health-15-minutes", 4, 5),            # -4 through -5
    # New themes
    ("clean-eating-on-a-budget", 1, 2),
    ("family-friendly-clean-eating", 1, 2),
    ("breakfast-made-easy", 1, 2),
    ("quick-dinner-solutions", 1, 2),
    ("one-pot-clean-eating", 1, 2),
    ("meal-prep-sunday-guide", 1, 2),
    ("sugar-detox-made-simple", 1, 2),
    ("gluten-free-clean-eating", 1, 2),
    ("high-protein-clean-eating", 1, 2),
    ("weight-loss-clean-eating", 1, 2),
    ("gut-health-clean-eating", 1, 2),
    ("clean-eating-starter-kit", 1, 2),
]

# Build full slug list
all_slugs = []
for base, start, end in slug_groups:
    for n in range(start, end + 1):
        all_slugs.append(f"{base}-{n}" if n > 1 else base)

# Verify count
assert len(all_slugs) >= 70, f"Need 70 slugs, only have {len(all_slugs)}"
all_slugs = all_slugs[:70]

# Template structure (matches existing landing pages)
template = """<!-- SYSTEME.IO COMPATIBLE SNIPPET - VARIATION {vid} -->
<style>
    #lp-organic-{vid} {{
        font-family: 'Segoe UI', Verdana, sans-serif;
        color: #2D3436;
        background: #FDFCF0;
        max-width: 800px;
        margin: 0 auto;
        padding: 0;
        line-height: 1.8;
        border: 1px solid #eee;
    }}
    #lp-organic-{vid} .header-container {{
        text-align: center;
        background: #E9EDC9;
        padding: 60px 20px;
        border-radius: 0 0 50px 50px;
    }}
    #lp-organic-{vid} h1 {{
        font-family: 'Georgia', serif;
        font-size: 2.5em;
        color: #606C38;
        margin: 0 0 10px;
        line-height: 1.2;
    }}
    #lp-organic-{vid} .subheadline {{
        color: #606C38;
        opacity: 0.8;
        font-size: 1.2em;
        margin-bottom: 20px;
    }}
    #lp-organic-{vid} .hero-img {{
        width: 100%;
        max-width: 600px;
        border-radius: 20px;
        display: block;
        margin: 30px auto;
        border: 10px solid #FEFAE0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }}
    #lp-organic-{vid} .cta-btn {{
        display: inline-block;
        background: #D4A373;
        color: #fff !important;
        text-decoration: none;
        padding: 22px 45px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.2em;
        margin: 25px 0;
        box-shadow: 0 5px 15px rgba(212, 163, 115, 0.3);
        border: none;
        cursor: pointer;
    }}
    #lp-organic-{vid} .section {{
        padding: 60px 20px;
        text-align: center;
    }}
    #lp-organic-{vid} .benefit-list {{
        text-align: left;
        display: inline-block;
        max-width: 500px;
        margin: 20px 0;
        list-style: none;
        padding: 0;
    }}
    #lp-organic-{vid} .benefit-list li {{
        margin-bottom: 12px;
        padding-left: 35px;
        position: relative;
    }}
    #lp-organic-{vid} .benefit-list li::before {{
        content: '\2713';
        position: absolute;
        left: 0;
        color: #606C38;
        font-weight: bold;
        font-size: 1.2em;
    }}
    #lp-organic-{vid} .bonus-section {{
        background: #E9EDC9;
        padding: 60px 40px;
        border-radius: 40px;
        margin: 40px 20px;
        text-align: center;
    }}
    #lp-organic-{vid} .bonus-badge {{
        background: #CCD5AE;
        color: #606C38;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 0.9em;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 20px;
    }}
    #lp-organic-{vid} .guarantee-box {{
        background: #fff;
        padding: 40px;
        border-radius: 30px;
        margin: 40px 20px;
        border: 2px solid #E9EDC9;
        text-align: left;
    }}
    #lp-organic-{vid} .guarantee-box h2 {{
        text-align: center;
        color: #606C38;
        font-family: 'Georgia', serif;
        margin-bottom: 30px;
    }}
    #lp-organic-{vid} .price {{
        font-size: 2.5em;
        color: #606C38;
        font-weight: bold;
        font-family: 'Georgia', serif;
        display: block;
        margin: 20px 0;
        text-align: center;
    }}
    #lp-organic-{vid} .footer {{
        padding: 40px 20px;
        text-align: center;
        color: #606C38;
        opacity: 0.6;
        font-size: 0.9em;
    }}
</style>

<div id="lp-organic-{vid}">
    <div class="header-container">
        <h1>{headline}</h1>
        <p class="subheadline">This comprehensive guide will help you:</p>
        <ul class="benefit-list">
            <li>Master the art of clean eating</li>
            <li>Create delicious, nutritious meals</li>
            <li>Achieve your weight loss goals</li>
            <li>Boost your energy levels</li>
            <li>Improve your overall health</li>
        </ul>
        <br>
        <a href="{checkout_link}" class="cta-btn">Get Access Now</a>
    </div>

    <div class="section">
        <h2>Introducing Clean Eating for Beginners</h2>
        <p>We've simplified clean eating into easy-to-follow steps, 75 delicious recipes, and a practical 21-day meal plan.</p>
        <p><strong>This isn't just a book; it's your personalized roadmap to wellness.</strong></p>
        
        <img src="{img1}" class="hero-img" alt="Healthy Lifestyle">
        
        <h3>In this book you will DISCOVER the power of clean eating to:</h3>
        <ul class="benefit-list">
            <li>Boost your energy levels</li>
            <li>Improve your digestion</li>
            <li>Enhance your skin and hair</li>
            <li>Lose weight effortlessly</li>
        </ul>
    </div>

    <div class="section" style="background: #FEFAE0;">
        <p>Our proven 21-day meal plan will guide you step-by-step, making it easy to incorporate delicious, nutritious meals into your daily routine. With 75 mouth-watering recipes, you'll never get bored.</p>
        
        <img src="{img2}" class="hero-img" alt="Recipe Preview">
        
        <h2>Here's what you'll learn:</h2>
        <ul class="benefit-list">
            <li>The science behind clean eating</li>
            <li>How to shop for healthy, affordable ingredients</li>
            <li>Simple meal prep tips to save time and energy</li>
            <li>Delicious recipes for breakfast, lunch, dinner, and snacks</li>
            <li>How to overcome common obstacles and stay on track</li>
        </ul>
    </div>

    <div class="bonus-section">
        <span class="bonus-badge">LIMITED TIME BONUS</span>
        <h2>But wait, there's more!</h2>
        <p>Order your copy NOW, and you'll receive a <strong>FREE consultation with a certified health and wellness coach</strong>. They'll provide personalized advice and support to help you achieve your health goals.</p>
        <p>Don't miss out on this incredible opportunity to transform your life.</p>
        <h3 style="color: #D4A373;">THIS BONUS DISAPPEARS AFTER THE NEXT 20 PEOPLE JOIN! ACT NOW!</h3>
        <p>Your 2026 journey to health starts here!</p>
        <a href="{checkout_link}" class="cta-btn">Get Access Now</a>
    </div>

    <div class="section">
        <p>All of this—and so much more—is yours when you download your copy of <strong>"Clean Eating for Beginners: 75 Recipes and 21-Day Meal Plan for Healthy Living."</strong></p>
        <img src="{img3}" class="hero-img" alt="Meal Plan">
    </div>

    <div class="guarantee-box">
        <h2>Still not convinced?</h2>
        <h3 style="text-align: center; color: #606C38;">My DOUBLE-DOUBLE GUARANTEE</h3>
        <p><strong>GUARANTEE #1:</strong> If for any reason this book isn't the best $7.99 you've ever spent, just send me an email and I'll gladly refund every penny...</p>
        <p><strong>GUARANTEE #2:</strong> If you actually USE the information in this system and your results aren't that great, I'll actually refund you - AND you can keep the program for free. Here's what you need to do: Just send me an email...</p>
        <p><em>All I ask is your best honest effort.</em></p>
        
        <div style="text-align: center;">
            <a href="{checkout_link}" class="cta-btn">Ok, I'll try it out!</a>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2026 Clean Eating Simplified. All rights reserved.</p>
    </div>
</div>
"""

# Generate pages
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
os.chdir(base_dir)

random.shuffle(new_headlines)
selected_headlines = new_headlines[:70]

created = 0
for i, slug in enumerate(all_slugs):
    vid = 51 + i
    headline = selected_headlines[i]
    img1, img2, img3 = pick_images()

    page_dir = os.path.join(base_dir, slug)
    os.makedirs(page_dir, exist_ok=True)

    content = template.format(
        vid=vid,
        headline=headline,
        img1=img1,
        img2=img2,
        img3=img3,
        checkout_link=checkout_link,
    )

    with open(os.path.join(page_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)

    created += 1
    print(f"  [{created:2d}/{len(all_slugs)}] {slug}/  (headline: {headline[:50]}...)")

print(f"\nDone! Created {created} new landing pages.")
print(f"Total pages now: {created + 53} (approx)")
