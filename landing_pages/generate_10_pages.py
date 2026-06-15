import os
import random

# Load Cloudinary Links
with open("cloudinary_links.txt", "r") as f:
    image_pool = [line.strip() for line in f if line.strip()]

# Remove known blurry or duplicate indices from pool if necessary
# Based on user feedback, 3 and 4 are identical, 5 and 6 are identical.
# I'll handle this in the selection logic to ensure they aren't on the same page.

checkout_link = "https://oliviaselfcare.gumroad.com/l/recepies?wanted=true"

# Headlines (keeping them natural and benefit-driven)
headlines = [
    "The 'Lazy Cook's' Guide to Healthy Eating: Simple Recipes for a Healthier You",
    "Stop Stressing About Dinner: The Lazy Cook's Roadmap to Clean Eating",
    "Finally, Clean Eating Made Effortless: A Beginner's Guide to Vibrant Health",
    "Your Mid-Year Reset Starts Today: Simple Recipes for the Busy Lazy Cook",
    "The Summer 2026 'Glow-Up' Roadmap: Effortless Clean Eating for Beginners",
    "Clean Eating for Beginners: 75 Simple Recipes for a Healthier You",
    "Boost Your Energy with the Lazy Cook's Plan: Simple Steps to Wellness",
    "Transform Your Lifestyle in Just 21 Days: The Lazy Cook's Recipe for Success",
    "No-Fuss Healthy Eating for Busy People: The Ultimate Lazy Cook's Guide",
    "The Easiest Way to Master Clean Eating: Simple Recipes for Beginners"
]

template = """<!-- SYSTEME.IO COMPATIBLE SNIPPET - VARIATION {id} -->
<style>
    #lp-organic-{id} {{
        font-family: 'Segoe UI', Verdana, sans-serif;
        color: #2D3436;
        background: #FDFCF0;
        max-width: 800px;
        margin: 0 auto;
        padding: 0;
        line-height: 1.8;
        border: 1px solid #eee;
    }}
    #lp-organic-{id} .header-container {{
        text-align: center;
        background: #E9EDC9;
        padding: 60px 20px;
        border-radius: 0 0 50px 50px;
    }}
    #lp-organic-{id} h1 {{
        font-family: 'Georgia', serif;
        font-size: 2.5em;
        color: #606C38;
        margin: 0 0 10px;
        line-height: 1.2;
    }}
    #lp-organic-{id} .subheadline {{
        color: #606C38;
        opacity: 0.8;
        font-size: 1.2em;
        margin-bottom: 20px;
    }}
    #lp-organic-{id} .hero-img {{
        width: 100%;
        max-width: 600px;
        border-radius: 20px;
        display: block;
        margin: 30px auto;
        border: 10px solid #FEFAE0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }}
    #lp-organic-{id} .cta-btn {{
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
    #lp-organic-{id} .section {{
        padding: 60px 20px;
        text-align: center;
    }}
    #lp-organic-{id} .benefit-list {{
        text-align: left;
        display: inline-block;
        max-width: 500px;
        margin: 20px 0;
        list-style: none;
        padding: 0;
    }}
    #lp-organic-{id} .benefit-list li {{
        margin-bottom: 12px;
        padding-left: 35px;
        position: relative;
    }}
    #lp-organic-{id} .benefit-list li::before {{
        content: '✓';
        position: absolute;
        left: 0;
        color: #606C38;
        font-weight: bold;
        font-size: 1.2em;
    }}
    #lp-organic-{id} .bonus-section {{
        background: #E9EDC9;
        padding: 60px 40px;
        border-radius: 40px;
        margin: 40px 20px;
        text-align: center;
    }}
    #lp-organic-{id} .bonus-badge {{
        background: #CCD5AE;
        color: #606C38;
        padding: 10px 20px;
        border-radius: 30px;
        font-size: 0.9em;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 20px;
    }}
    #lp-organic-{id} .guarantee-box {{
        background: #fff;
        padding: 40px;
        border-radius: 30px;
        margin: 40px 20px;
        border: 2px solid #E9EDC9;
        text-align: left;
    }}
    #lp-organic-{id} .guarantee-box h2 {{
        text-align: center;
        color: #606C38;
        font-family: 'Georgia', serif;
        margin-bottom: 30px;
    }}
    #lp-organic-{id} .price {{
        font-size: 2.5em;
        color: #606C38;
        font-weight: bold;
        font-family: 'Georgia', serif;
        display: block;
        margin: 20px 0;
        text-align: center;
    }}
    #lp-organic-{id} .footer {{
        padding: 40px 20px;
        text-align: center;
        color: #606C38;
        opacity: 0.6;
        font-size: 0.9em;
    }}
</style>

<div id="lp-organic-{id}">
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
        <p>We’ve simplified clean eating into easy-to-follow steps, 75 delicious recipes, and a practical 21-day meal plan.</p>
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
        <p>All of this—and so much more—is yours when you download your copy of <strong>“Clean Eating for Beginners: 75 Recipes and 21-Day Meal Plan for Healthy Living.”</strong></p>
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

os.makedirs("landing_pages", exist_ok=True)

# Image map to indices for duplicate check
# Links are 0-indexed in image_pool
# 3 and 4 are identical, 5 and 6 are identical.
# Actually let's just use the links themselves.
link_to_id = {link: i+1 for i, link in enumerate(image_pool)}

for i in range(1, 11):
    # Select 3 unique images
    selected_images = []
    temp_pool = list(image_pool)
    random.shuffle(temp_pool)
    
    for link in temp_pool:
        idx = link_to_id[link]
        # Check for user-defined duplicates on same page
        forbidden = []
        if idx == 3: forbidden.append(4)
        if idx == 4: forbidden.append(3)
        if idx == 5: forbidden.append(6)
        if idx == 6: forbidden.append(5)
        
        # Check if any forbidden index is already in selected_images
        already_selected_ids = [link_to_id[l] for l in selected_images]
        if not any(f in already_selected_ids for f in forbidden):
            selected_images.append(link)
        
        if len(selected_images) == 3:
            break
            
    headline = headlines[i-1] # Use unique headlines for first 10
    
    content = template.format(
        id=i,
        headline=headline,
        img1=selected_images[0],
        img2=selected_images[1],
        img3=selected_images[2],
        checkout_link=checkout_link
    )
    
    with open(f"landing_pages/variation_{i}.html", "w", encoding="utf-8") as f:
        f.write(content)

print("Generated first 10 variations in 'landing_pages' folder.")
