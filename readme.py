#!/usr/bin/python

import re
import random

alternatives_bracket = re.compile(r'\[([^/]*)/([^\]]*)\]') # thar be dragons! explanation:

#  \[   open bracket
#  ([^/]*)   first group, goes up to a slash
#  /    the slash
# ([^\]]*)  second group, goes up to the closing bracket
#  \]   closing bracket

# so it parses things of the form [first group/second group]

def choose_one(match_object):
    return match_object.group(random.choice([1,2]))

def process_brackets(text_to_process):
    return alternatives_bracket.sub(choose_one,text_to_process)

print process_brackets("""Content-type: text/html

<html>
<head>
    <title>[The /]Fifth Dimensional Chaos Matrix[, The/]</title>
</head>
<body>

<p>[Hello/Welcome][!/!!][!/]</p>

<p>[This is/You have reached] [the/a] [homepage/webpage] for 
[the /]Fifth Dimensional Chaos Matrix, [a Discordian/an Erisian] 
[programming/software] project[./!]</p>

<p>The [founder/originator] of this [project/program] is 
[Brett Douglas Williams/Pope Salmon the Lesser Mungojelly], 
who [can be reached/you can reach] at 
<a href="mailto:mungojelly@gmail.com">mungojelly@gmail.com</a>[./!]</p>

<p>[The /]Fifth Dimensional Chaos Matrix is named [after/following] the 
<a href="http://jubal.westnet.com/hyperdiscordia/hodge_podge_transformer.gif">diagram</a> 
in the <a href="http://jubal.westnet.com/hyperdiscordia/hodge_podge.html">Hodge-Podge</a> 
[section/part] of the 
<a href="http://en.wikipedia.org/wiki/Principia_Discordia">Principia Discordia</a>[./!]</p>

<p>The [intention/aim] of [this project/FDCM] [is not/isn't] to [make/create] something 
[useful/practical][./!]  [It is/It's] an exp[eriment/loration][./!]</p>

<p>[FDCM/Fifth Dimensional Chaos Matrix] [mak/creat]es chaos [from/out of] order and 
order [from/out of] chaos[./!]</p>

<p>[You're free/Feel free] to [contribute/write] [parts/components] for [FDCM/Fifth Dimensional 
Chaos Matrix][./!]  ([Which/That] [should/ought to] be [fairly/relatively] easy, since 
[parts/components] of the [FDCM/Fifth Dimensional Chaos Matrix] don't [even /]necessarily 
[need/have] to do [anything/something] [coherent/predictable][./!])</p>

<p>This [page/description] [changes/transforms] [each/every] time [it's/it is] 
[viewed/reloaded][./!]  Its <a 
href="http://github.com/mungojelly/Fifth-Dimensional-Chaos-Matrix/blob/master/readme.py">
[code/source]</a> [is included/can be found] [at/with] [its/the] 
<a href="http://github.com/mungojelly/Fifth-Dimensional-Chaos-Matrix">GitHub project</a>[./!]
</p>

<p>[Thanks/Thank you] for your [interest/attention][./!]</p>

<p>&lt;3[!/][!/]</p>

</body>
</html>
""")

