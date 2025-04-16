import subprocess

packages = [
    "beautifulsoup4==4.12.2",
    "certifi==2023.5.7",
    "charset-normalizer==3.1.0",
    "click==8.1.3",
    "colorama==0.4.6",
    # "dgl==1.1.0",  # Uncomment if needed
    "Flask==2.2.2",
    "idna==3.4",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "joblib==1.2.0",
    "MarkupSafe==2.1.1",
    "nltk==3.8.1",
    "numpy==1.23.1",
    "pandas==1.5.1",
    "psutil==5.9.5",
    "python-dateutil==2.8.2",
    "pytz==2022.5",
    "regex==2023.8.8",
    "requests==2.31.0",
    "scikit-learn==1.2.0",
    "scipy==1.9.3",
    "six==1.16.0",
    "soupsieve==2.4.1",
    "threadpoolctl==3.1.0",
    "tqdm==4.65.0",
    "urllib3==2.0.3",
    "Werkzeug==2.2.2"
]

for pkg in packages:
    print(f"\n📦 Installing: {pkg}")
    try:
        subprocess.check_call(["pip", "install", pkg])
        print(f"✅ Installed: {pkg}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install: {pkg}")
