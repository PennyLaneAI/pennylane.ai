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
        "Check our our <a href=\"attractions.html\">attractions</a> page for more details."
        "Also watch out for special announcements throughout the month."
    ),
    (
        "Is there a deadline for registration?",
        "..."
    ),
    (
        "Does it cost anything to attend QHack?",
        "No, attendance is FREE for everyone!"
    ),
    (
        "What is the format for the hackathon?",
        "The <a href=\"https://qhack.ai/hackathon.html\">hackathon</a> will consist of two stages. "
        "In the <span style=\"font-weight: bold; font-style: italic;\">QML Challenge Board</span>, "
        "you will tackle a set of quantum machine learning questions of various difficulty levels. "
        "In the <span style=\"font-weight: bold; font-style: italic;\">QHack Open Hackathon</span>, teams will have one week to build a free-form "
        "hackathon project. More details can be found <a href=\"https://github.com/XanaduAI/QHack2021\">here</a>. "
    ),
    (
        "Are there prizes?",
        "Yes! Check <a href=\"https://qhack.ai/hackathon.html\">here</a> for an overview of the hackathon prizes and power ups."
    ),
    (
        "How do I know if I have been successfully registered?",
        "Everyone who has submitted the registration form is on the attendees list. "
        "There are no special acceptance criteria."
    ),
    (
        "How do I sign into the QML Challenge web portal?",
        "The web portal can be accessed <a href=\"https://challenge.qhack.ai/\">here</a>. "
        "You will need to register your Team in order to be able to submit your solutions "
        "and claim your points. There can only be one account associated with each Team, "
        "so if you're a Team of more than one person you should designate someone as Team Captain "
        "to register on behalf of the Team and submit the Team's solutions."
    ),
    (
        "My team name has already been taken! What do I do?",
        "Team names are unique. The only way to guarantee your favourite name in the "
        "QML Challenge web portal is to create an account and grab it early. "
        "If your team has multiple members, check if one of your teammates has already "
        "created an account."
    ),
    (
        "What is the maximum team size?",
        "We recommend a maximum team size of 3 people. Teams of 4+ may also be acceptable, "
        "but the CERN internship prize has a maximum of three positions available."
    ),
    (
        "Do I have to form a team?",
        "No. Individuals can take part in the hackathon challenges independently. "
        "There is no distinction on the scoreboard between teams of one or teams with multiple members. "
        "Attendees can also choose to follow our livestream content without taking "
        "on the hackathon challenges (though we encourage you to do so!)."
    ),
    (
        "How do I find a team?",
        "Recruit friends, work colleagues, classmates, or put the call out in existing communities "
        "such as the <a href=\"https://discuss.pennylane.ai\">PennyLane discussion forum</a>, "
        "the <a href=\"https://xanadu-quantum.slack.com/\">Xanadu Slack</a>, "
        "the <a href=\"https://discord.gg/JqVGmpkP96\">Unitary Fund Discord</a>, or "
        "the <a href=\"https://qosf.slack.com\">QOSF Slack</a>."
    ),
    (
        "What skill level do I need to have to participate?",
        "We are aiming to offer something for everyone, from complete beginners "
        "to seasoned experts. As part of the event, we will provide introductory tutorials for "
        "quantum machine learning and for programming quantum computers."
    ),
    (
        "What software do I need to use for the hackathon?",
        "Our hackathon challenges will be based on <a href=\"https://pennylane.ai\">PennyLane</a> and "
        "<a href=\"https://aws.amazon.com/braket\">Amazon Braket</a>."
    ),
    (
        "Where can I get help with my AWS account or Amazon Braket?",
        "We've set up two dedicated channels for AWS and Amazon Braket support on the <a href=\"https://join.slack.com/t/xanadu-quantum/shared_invite/zt-lxv8gwbp-e_KN6iXMfrxLoa26nPYzYg\">Xanadu Slack</a>. "
        "For general AWS Support, submit questions to the <em>#aws-general-support</em> channel. " 
        "For support questions specific to Amazon Braket please join the <em>#amazon-braket-support</em> channel."
    ),
    (
        "Are there example challenge questions I can look at?",
        "We will not be sharing specific example questions before the event. "
        "To best prepare, the ideal source of example material is the PennyLane "
        "<a href=\"https://pennylane.ai/qml\">QML website</a>."
    ),
    (
        "What is the expected workload for completing the hackathon questions?",
        "Multiple hackathon questions will be available, with different levels of difficulty. "
        "It is up to you how much time you would like to put in; simply choose a question "
        "to start with, and go from there! There is no requirement to answer every question."
    ),
    (
        "When will my SWAG pack arrive?",
        "We have provided SWAG packs to a limited number of early-bird attendees. "
        "These were mailed out several weeks before the event. "
        "While we hope that SWAG packs arrived in a timely manner, please note that "
        "postal delays could cause packs to arrive later than expected."
    ),
    (
        "How can I connect with others who are taking part in QHack?",
        "For general discussion about QHack, join the <a href=\"https://join.slack.com/t/xanadu-quantum/shared_invite/zt-lxv8gwbp-e_KN6iXMfrxLoa26nPYzYg\">Xanadu Slack</a> "
        "and introduce yourself on the <a href=\"https://xanadu-quantum.slack.com/archives/C01JZT78KC6\">#qhack channel</a>."
    ),
    (
        "Will the talks be recorded and available later?",
        "Yes. The talks will be available as videos-on-demand shortly after airing. "
        "We will also be replaying some of the day's highlights starting at 9PM EST. "
        "The talks will be re-posted on other channels at a later time."
    )
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
        },
        "install.html": {
            "install_page": True,
            "title": "Install &#8212; PennyLane",
            "canonical_url": "https://pennylane.ai/install.html",
            "description": "See how to install PennyLane and its plugins. Install the pip package, "
                           "build from the latest GitHub source code, and get the one-line command "
                           "for installing all plugins.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
        },
        "plugins.html": {
            "plugins_page": True,
            "title": "Plugins and ecosystem &#8212; PennyLane",
            "canonical_url": "https://pennylane.ai/plugins.html",
            "description": "See the avilable PennyLane plugins, allowing access to quantum simulators "
                           "and hardware from IBM, Rigetti, Google, and more.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
        },
        "faq.html": {
            "faq_page": True,
            "title": "Frequently Asked Questions (FAQ) &#8212; PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/faq.html",
            "description": "Curious? Find all the details about PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/thumbnail.png",
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
        },
        "carnival/index.html": {
            "title": "PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Join us for the PennyLane Quantum Carnival, "
                           "running throughout the month of November 2021.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "faq": FAQ,
        },
        "carnival/attractions.html": {
            "title": "PennyLane Quantum Carnival &#8212; Attractions",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Check out all the events taking place during "
                           "the PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
        },
        "carnival/talent_show.html": {
            "title": "PennyLane Quantum Carnival &#8212; Talent Show",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Step right up and show us what you've got. "
                           "Submit your most creative work to our quantum Talent Show.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
        },
        "carnival/scavenger_hunt.html": {
            "title": "PennyLane Quantum Carnival &#8212; Scavenger Hunt",
            "canonical_url": "https://pennylane.ai/carnival/index.html",
            "description": "Take part in our festivities, collect tickets, "
                           "and trade them in for prizes.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
        },
        "carnival/faq.html": {
            "faq_page": True,
            "title": "Frequently Asked Questions (FAQ) &#8212; PennyLane Quantum Carnival",
            "canonical_url": "https://pennylane.ai/carnival/faq.html",
            "description": "Curious? Find all the details about PennyLane Quantum Carnival.",
            "thumbnail": "https://pennylane.ai/img/carnival_splash.png",
            "faq": FAQ,
        },
    }

    for file in files:
        with open(f"site/{file}", "w") as f:
            f.write(render_from_template("jinja", file, **files[file]))


if __name__ == "__main__":
    render_templates()
