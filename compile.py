#!/usr/bin/env python

from jinja2 import FileSystemLoader, Environment


def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

FAQ = [
        (
        "When will PennyLane Quantum Carnival take place?",
        "November 1-30, 2021. "
    ),
    (
        "What is the schedule?",
        "Check our our <a href=\"attractions.html\">attractions</a> page for more details. "
        "Also watch out for special announcements throughout the month."
    ),
    (
        "Is there a deadline for registration?",
        "November 30th 2021 11:59pm ET"
    ),
    (
        "Are there prizes?",
        "Absolutely! The prize booth will become available during the event. "
        "Check <a href=\"scavenger_hunt.html\">here</a> for more "
        "details on how to win prizes."
    ),
    (
        "How do I know if I have been successfully registered?",
        "You should have seen a confirmation message on your screen after submitting "
        "our <a href=\"register.html\">sign-up form</a>."
    ),
    (
        "Do I need to register in order to participate in the Talent Show?",
        "Yes, you will need to <a href=\"register.html\">register</a> for "
        "the Carnival before submitting your entry to the Talent Show. "
        "All we need is your email."
    ),
    (
        "How do I get tickets in the Scavenger Hunt?",
        "You can get tickets by attending our live events, contributing to "
        "PennyLane, participating in the Talent Show, and if you search carefully, "
        "you can find many other tickets hidden in secret places."
    ),
    (
        "How many events are there?",
        "Several key events are listed on the "
        "<a href=\"attractions.html\">attractions page</a>. "
        "Other announcements will be made on the PennyLane Twitter account, so "
        "<a href=\"https://twitter.com/intent/user?screen_name=pennylaneai\">follow us</a> "
        "to stay informed. "
        "When you <a href=\"register.html\">register</a> you will also have the option "
        "to receive email notifications with updates about the Carnival."
    ),
    (
        "How many tickets are there in total?",
        "In total, there are 100 unique points which can be won by earning "
        "or finding tickets."
    ),
]


def render_templates():
    files = {
        "index.html": {
            "index_page": True,
            "title": "PennyLane",
            "canonical_url": "https://pennylane.ai",
            "description": "A Python library for quantum machine learning, automatic differentiation, "
                           "and optimization of hybrid quantum-classical computations. Use multiple "
                           "hardware devices, alongside TensorFlow or PyTorch, in a single computation.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
            "root": "."
        },
        "install.html": {
            "install_page": True,
            "title": "Install &#8212; PennyLane",
            "canonical_url": "https://pennylane.ai/install.html",
            "description": "See how to install PennyLane and its plugins. Install the pip package, "
                           "build from the latest GitHub source code, and get the one-line command "
                           "for installing all plugins.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
            "root": "."
        },
        "plugins.html": {
            "plugins_page": True,
            "title": "Plugins and ecosystem &#8212; PennyLane",
            "canonical_url": "https://pennylane.ai/plugins.html",
            "description": "See the avilable PennyLane plugins, allowing access to quantum simulators "
                           "and hardware from IBM, Rigetti, Google, and more.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
            "root": "."
        },
        "faq.html": {
            "faq_page": True,
            "title": "Frequently Asked Questions (FAQ) &#8212; PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/faq.html",
            "description": "Curious? Find all the details about PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
            "root": ".",
            "faq": FAQ,
        },
        "404.html": {
            "404_page": True,
            "title": "Page not found &#8212; PennyLane",
            "canonical_url": "https://pennylane.ai/404.html",
            "description": "A Python library for quantum machine learning, automatic differentiation, "
                           "and optimization of hybrid quantum-classical computations. Use multiple "
                           "hardware devices, alongside TensorFlow or PyTorch, in a single computation.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
            "root": "."
        },
        "carnival/index.html": {
            "title": "PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Join us for the PennyLane Quantum Carnival, "
                           "running throughout the month of November 2021.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "faq": FAQ,
            "root": ".."
        },
        "carnival/attractions.html": {
            "title": "PennyLane Quantum Carnival &#8212; Attractions",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Check out all the events taking place during "
                           "the PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "root": ".."
        },
        "carnival/talent_show.html": {
            "title": "PennyLane Quantum Carnival &#8212; Talent Show",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Step right up and show us what you've got. "
                           "Submit your most creative work to our quantum Talent Show.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "root": ".."
        },
        "carnival/scavenger_hunt.html": {
            "title": "PennyLane Quantum Carnival &#8212; Scavenger Hunt",
            "canonical_url": "https://pennylane.ai/carnival/scavenger_hunt.html",
            "description": "Take part in our festivities, collect tickets, "
                           "and trade them in for prizes.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "root": ".."
        },
        "carnival/faq.html": {
            "faq_page": True,
            "title": "Frequently Asked Questions (FAQ) &#8212; PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/faq.html",
            "description": "Curious? Find all the details about PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "faq": FAQ,
            "root": ".."
        },
        "carnival/register.html": {
            "title": "Register &#8212; PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/register.html",
            "description": "Sign up for the PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "root": ".."
        },
        "carnival/claim.html": {
            "title": "Claim a prize &#8212; PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/register.html",
            "description": "Redeem your tickets to claim a prize in the PennyLane Quantum Carnival Scavenger Hunt.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "root": ".."
        },
    }

    for file in files:
        with open(f"site/{file}", "w") as f:
            f.write(render_from_template("jinja", file, **files[file]))


if __name__ == "__main__":
    render_templates()
