#!/usr/bin/env python

from jinja2 import FileSystemLoader, Environment


def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)


FAQ = [
    (
        "What is PennyLane?",
        "PennyLane is a <b> software framework for differentiable quantum programming</b>, "
        "similar to TensorFlow and PyTorch for classical computation. It facilitates the "
        "training of variational quantum circuits."
    ),
    (
        "Does PennyLane work with hardware?",
        "Yes, PennyLane can be used to optimize quantum circuits running on hardware. "
        "Simply choose a hardware backend as your device. You can find all available backends "
        "in the <a href=\"plugins.html\">plugins</a> section."
    ),
    (
         "Can I use PennyLane with PyTorch/TensorFlow?",
         "Yes, PennyLane integrates with PyTorch and TensorFlow. More information can be found "
         "in the <a href=\"https://pennylane.readthedocs.io\">documentation</a>."
    ),
    (
        "What distinguishes PennyLane from other quantum programming languages?",
        "While offering a lot of the functionality of standard quantum programming languages, "
        "PennyLane is built around the idea of <b> training quantum circuits using automatic "
        "differentiation</b>. This is especially important in applications such as quantum "
        "machine learning, quantum chemistry, and quantum optimization."
    ),
    (
        "What is quantum machine learning?",
        "Quantum machine learning investigates the <b>consequences of using quantum computers "
        "for machine learning</b>, by extending the pool of hardware for machine learning by "
        "an entirely new type of computing device—the quantum computer.<br><br>"
        "One can understand these devices as a form of special-purpose hardware like Application-Specific "
        "Integrated Circuits (ASICs) and Field-Programmable Gate Arrays (FPGAs), as they are limited in "
        "the number and type of operations that can be executed in a single run. However, information processing "
        "with quantum computers relies on substantially different laws of physics compared to ASICs and FPGAs. <br><br>"
        "In modern quantum machine learning, near-term quantum devices are used and trained like neural networks, "
        "using <b>variational quantum circuits</b>. "
        "More information can be found in our <a href=\"https://pennylane.ai/qml/whatisqml.html\">What is QML?</a> "
        "page."
    ),
    (
        "What are variational circuits?",
        "Variational quantum circuits, also called parametrized quantum circuits, are "
        "<b>quantum algorithms that depend on tunable parameters</b>. <br><br>"
        "For example consider a quantum algorithm where one operation rotates a qubit by a "
        "certain angle kept as a free parameter. The result of the quantum computation now "
        "depends on the chosen angle. Using a classical co-processor, the angle, and thereby "
        "the quantum circuit, can be <b>optimized for a given task</b>. <br><br>"
        "The principle of variational circuits is very similar to neural networks, which is "
        "why they play an important role in quantum machine learning.<br><br>"
        "Visit our <a href=\"https://pennylane.ai/qml/glossary.html\">QML glossary</a> for more information "
        "on the key concepts underpinning quantum machine learning."
    ),
    (
        "How does PennyLane evaluate gradients of quantum circuits?",
        "Wherever possible, <b>PennyLane uses parameter-shift rules</b> to extract gradients of "
        "quantum circuits. These rules prescribe how to estimate a gradient by running a circuit "
        "twice or more times with deliberately shifted parameters. <br><br> In situations where "
        "no parameter-shift rule can be applied, PennyLane uses the finite-difference rule to "
        "approximate a gradient. <br><br> Both options work whether you run your code on simulators or "
        "an actual quantum device.<br><br>"
        "Visit our <a href=\"https://pennylane.ai/qml/glossary.html\">QML glossary</a> for more information "
        "on the key concepts underpinning quantum machine learning."
    ),
    (
        "Is PennyLane open source?",
        "Yes, PennyLane is open source software developed under the Apache 2.0 License."
    )
]


CARNIVAL_FAQ = [
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
        "November 30th 2021 5:59pm ET"
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
            "title": "Frequently Asked Questions (FAQ) &#8212; PennyLane", 
            "canonical_url": "https://pennylane.ai/faq.html", 
            "description": "Get quick answers to your most burning questions on PennyLane and " 
                           "quantum machine learning.", 
            "thumbnail": "https://pennylane.ai/img/thumbnail.png", 
            "faq": FAQ,
            "root": "."
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
        ##########################
        # Carnival pages
        ##########################
#        "carnival/index.html": {
#            "title": "PennyLane Quantum Carnival",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Join us for the PennyLane Quantum Carnival, "
#                           "running throughout the month of November 2021.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "faq": FAQ,
#            "root": ".."
#        },
#        "carnival/attractions.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Attractions",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Check out all the events taking place during "
#                           "the PennyLane Quantum Carnival.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/talent_show.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Talent Show",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Step right up and show us what you've got. "
#                           "Submit your most creative work to our quantum Talent Show.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/scavenger_hunt.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Scavenger Hunt",
#            "canonical_url": "https://pennylane.ai/carnival/scavenger_hunt.html",
#            "description": "Take part in our festivities, collect tickets, "
#                           "and trade them in for prizes.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/faq.html": {
#            "faq_page": True,
#            "title": "Frequently Asked Questions (FAQ) &#8212; PennyLane Quantum Carnival",
#            "canonical_url": "https://pennylane.ai/carnival/faq.html",
#            "description": "Curious? Find all the details about PennyLane Quantum Carnival.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "faq": CARNIVAL_FAQ,
#            "root": ".."
#        },
#        "carnival/register.html": {
#            "title": "Register &#8212; PennyLane Quantum Carnival",
#            "canonical_url": "https://pennylane.ai/carnival/register.html",
#            "description": "Sign up for the PennyLane Quantum Carnival.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/claim.html": {
#            "title": "Claim a prize &#8212; PennyLane Quantum Carnival",
#            "canonical_url": "https://pennylane.ai/carnival/register.html",
#            "description": "Redeem your tickets to claim a prize in the PennyLane Quantum Carnival Scavenger Hunt.",
#            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
#            "root": ".."
#        },
#        "carnival/terms_and_conditions.html": {
#            "title": "Terms and Conditions &#8212; PennyLane Quantum Carnival",
#            "canonical_url": "https://pennylane.ai/carnival/terms_and_conditions.html",
#            "description": "Terms and Conditions for the PennyLane Quantum Carnival.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/trivia_party.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Trivia Party",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Have fun and join the party! "
#                           "Test yourself and get carnival tickets!",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/community_calls.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Community Calls",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Join us and get carnival tickets!",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/prize_booth.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Prize Booth",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Collect carnival tickets and earn these amazing prizes!",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
#        "carnival/coding_challenges.html": {
#            "title": "PennyLane Quantum Carnival &#8212; Coding Challenges",
#            "canonical_url": "https://pennylane.ai/carnival/index.html",
#            "description": "Try your hand at the PennyLane Quantum Carnival coding challenges.",
#            "thumbnail": "https://pennylane.ai/img/carnival_logo_splash.png",
#            "root": ".."
#        },
    }

    for file in files:
        with open(f"site/{file}", "w") as f:
            f.write(render_from_template("jinja", file, **files[file]))


if __name__ == "__main__":
    render_templates()
