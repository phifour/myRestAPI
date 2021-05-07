from flask import Flask
from transformers import pipeline

app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello, World!"


@app.route('/user/<username>')
def profile(username):
    return username


@app.route('/qa', methods=['GET'])
def getMessage():
    summarizer = pipeline("summarization")
    ARTICLE = """
    Albatrosses are very large seabirds in the family Diomedeidae. They range widely in the Southern Ocean and the North Pacific. They are absent from the North Atlantic, although fossil remains show they once occurred there and occasional vagrants are found. Albatrosses are among the largest of flying birds, and species of the genus Diomedea (great albatrosses) have the longest wingspans of any extant birds, reaching up to 3.7 m (12 ft). Albatrosses are usually regarded as falling into four genera, but disagreement exists over the number of species.
    Albatrosses are the most efficient travelers of all vertebrates on the planet. They expend very little energy soaring hundreds of miles over the ocean each day using dynamic soaring and slope soaring. They have a tendon in each shoulder locking their wings fully-extended, so once aloft and soaring across a fair breeze they never need to flap their wings. Like some vultures they hunt by smell, sensitive to the odor of carrion and other biological processes. 
    They feed on squid, fish, and krill by either scavenging, surface seizing, or diving. Albatrosses are colonial, nesting for the most part on remote oceanic islands, often with several species nesting together. Pair bonds between males and females form over several years, with the use of "ritualised dances", and last for the life of the pair. A breeding season can take over a year from laying to fledging, with a single egg laid in each breeding attempt. A Laysan albatross, named Wisdom, on Midway Island is the oldest-known wild bird in the world; she was first banded in 1956 by Chandler Robbins.
    Of the 22 species of albatrosses recognised by the IUCN, all are listed as at some level of concern; three species are critically endangered, five species are endangered, seven species are near threatened, and seven species are vulnerable. Numbers of albatrosses have declined in the past due to harvesting for feathers. Albatrosses are threatened by introduced species, such as rats and feral cats that attack eggs, chicks, and nesting adults; by pollution; by a serious decline in fish stocks in many regions largely due to overfishing; and by longline fishing. Longline fisheries pose the greatest threat, 
    as feeding birds are attracted to the bait, become hooked on the lines, and drown. Identified stakeholders such as governments, conservation organisations, and people in the fishing industry are all working toward reducing this bycatch.
    The "albatross" designation comprises between 13 and 24 species (the number is still a matter of some debate, with 21 being the most commonly accepted number) in four genera. These genera are the great albatrosses (Diomedea), the mollymawks (Thalassarche), 
    the North Pacific albatrosses (Phoebastria), and the sooty albatrosses or sooties (Phoebetria). The North Pacific albatrosses are considered to be a sister taxon to the great albatrosses, while the sooty albatrosses are considered closer to the mollymawks.The taxonomy of the albatross group has been a source of much debate. The Sibley-Ahlquist taxonomy places seabirds, birds of prey, and many others in a greatly enlarged order, the Ciconiiformes, whereas the ornithological organisations in North America, Europe, South Africa, Australia, and New Zealand retain the more traditional order Procellariiformes. 
    The albatrosses can be separated from the other Procellariiformes both genetically and through morphological characteristics, size, their legs, and the arrangement of their nasal tubes (see below: Morphology and flight).Within the family, the assignment of genera has been debated for over 100 years. 
    Originally placed into a single genus, Diomedea, they were rearranged by Reichenbach into four different genera in 1852, then lumped back together and split apart again several times, acquiring 12 different genus names in total (though never more than eight at one time) by 1965 (Diomedea, Phoebastria, Thalassarche, Phoebetria, Thalassageron, Diomedella, Nealbatrus, Rhothonia, Julietata, Galapagornis, Laysanornis, and Penthirenia).
    """
    summary = summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False)

    # print(summary[0]['summary_text'])

    return summary[0]['summary_text']
