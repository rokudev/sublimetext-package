import json

def listToRegexStr(list):
    result = "(?i:\\\\b("

    for item in sorted(list):
        result += "" + item + "|"

    result = result[:-1]
    result += ")\\\\b)"
    return result

def listToRegexAfterDotStr(list):
    result = "(?i:\\\\b\.("

    for item in sorted(list):
        result += "" + item + "|"

    result = result[:-1]
    result += ")\\\\b)"
    return result

def writeln(file, text):
    file.write(text+"\n")

brightScript_cson_file = open("Atom/grammars/brightscript.cson", "w")
brightScript_tmLanguage_file = open("Sublime/brightscript.tmLanguage", "w")
writeln(brightScript_tmLanguage_file,
    """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
\t<key>comment</key>
\t<string>BrightScript Language File</string>
\t<key>name</key>
\t<string>BrightScript</string>""")

name = "BrightScript"
brightScript_cson_file.write("name: \""+name+"\"\n")

# Comment
comment = "BRS Language"
brightScript_cson_file.write("comment: \""+comment+"\"\n")

# File names
brightScript_cson_file.write("fileTypes: [\n")
writeln(brightScript_tmLanguage_file,
"""\t<key>fileTypes</key>
\t<array>""")
fileTypes = ["brs", "bs"]
for fileType in fileTypes:
    brightScript_cson_file.write("\t\""+fileType+"\"\n")
    writeln(brightScript_tmLanguage_file, "\t\t<string>"+fileType+"</string>")
brightScript_cson_file.write("]\n")
writeln(brightScript_tmLanguage_file, "\t</array>")

# writeln(brightScript_tmLanguage_file, "\t</array>")

# Scope name
scopeName = "source.brightscript"
brightScript_cson_file.write("scopeName: \""+scopeName+"\"\n")
writeln(brightScript_tmLanguage_file,
    """\t<key>scopeName</key>
\t<string>"""+scopeName+"</string>")


# Start markers
foldingStartMarker = ["sub", "if", "for", "for each", "function", "while"]
foldingStartMarkerRegex = "foldingStartMarker: \"" + listToRegexStr(foldingStartMarker) + "\""
writeln(brightScript_cson_file, foldingStartMarkerRegex)
writeln(brightScript_tmLanguage_file, "\t<key>foldingStartMarker</key>")
writeln(brightScript_tmLanguage_file, "\t<string>"+listToRegexStr(foldingStartMarker).replace("\\\\", "\\")+"</string>")
# brightScript_cson_file.write(foldingStartMarkerRegex)

# Stop markers
foldingStopMarker = ["next", "end", "end if", "end sub", "end for", "end while", "end function"]
foldingStopMarkerRegex = "foldingStopMarker: \"" + listToRegexStr(foldingStopMarker) + "\""
# brightScript_cson_file.write(foldingStopMarkerRegex)
writeln(brightScript_cson_file, foldingStopMarkerRegex) # atom
writeln(brightScript_tmLanguage_file, "\t<key>foldingStopMarker</key>") # sublime
writeln(brightScript_tmLanguage_file, "\t<string>"+listToRegexStr(foldingStopMarker).replace("\\\\", "\\")+"</string>") # sublime

# program_statements
programStatementsRegex = listToRegexStr(foldingStartMarker+foldingStopMarker+["then", "return", "else", "stop", "step", "as", "each", "in",  "to"])

# constants
constantsRegex = listToRegexStr(["invalid", "true", "false", "[0-9]+"])

# operators and bool
operatorsRegex = "=|&gt;=|&lt;zz|&gt;|&lt;|&lt;&gt;|\\\\+|-|\\\\*|\\\\/|\\\\^|&amp;|\\\\\\\\b(?i:(And|Not|Or))\\\\\\\\b"

#
# Dynamic items from Confluence
#

#
# ###
#
# SDK 1 Nodes
#
fileToOpen = 'json/RokuComponents.json'

dataFile = open(fileToOpen, 'rb')

dataFileText = dataFile.read()
dataFileText = unicode(dataFileText, errors='ignore')
j = json.loads(dataFileText)

setOfAttributes = set()

for item in j['Events']:
    setOfAttributes.add(item)

sdk1EventsMatch = listToRegexStr(setOfAttributes)

for item in j['Interfaces']:
    # print item
    setOfAttributes.add(item)
# print j['Interfaces']["ifInt"]

sdk1InterfacesMatch = listToRegexStr(setOfAttributes)

brs_components = open("Atom/snippets/brs_components.cson", "w")
writeln(brs_components, "'.source.brightscript':")
for item in j['Components']:
    # TODO Sublime here
    # print "\"" + item + "\","
    setOfAttributes.add(item)
    writeln(brs_components, "\t'c_"+item+"':")
    writeln(brs_components, "\t\t'prefix':'CreateObject(\""+j['Components'][item]["name"]+"\")'")
    writeln(brs_components, "\t\t'body':'CreateObject(\""+j['Components'][item]["name"]+"\")'")
    writeln(brs_components, "\t\t'description':\"\"\"\n"+j['Components'][item]["description"]+"\n\"\"\"")
    writeln(brs_components, "\t\t'descriptionMoreURL':'"+j['Components'][item]["documentationURL"]+"'")


sdk1ComponentsMatch = listToRegexStr(setOfAttributes)
# SDK 1 Nodes


#
# ###
#
# SDK 2 Attributes regex
#
fileToOpen = 'json/RokuSceneGraph.json'

dataFile = open(fileToOpen, 'rb')

dataFileText = dataFile.read()

j = json.loads(dataFileText)

setOfAttributes = set()

for item in j['brightScriptNodes']:
    for attribute in j['brightScriptNodes'][item]["attributeNames"]:
        # print attribute
        setOfAttributes.add(attribute)

sdk2AttributesMatch = listToRegexAfterDotStr(setOfAttributes)

# SDK 2 Attributes regex

# TODO Literals
# TODO Operators
# TODO Types
# TODO Strings


repositories = {
        "program_statements"    : {
            "name"      : "keyword.control.brightscript",
            "match"     : programStatementsRegex
        },
        "constants"    : {
            "name"      : "constant.numeric.brightscript",
            "match"     : constantsRegex
        },
        "operators"    : {
            "name"      : "keyword.operator.brightscript",
            "match"     : operatorsRegex
        },
        "sdk1_components"       : {
            "name"      : "support.class.brightscript",
            "match"     : sdk1ComponentsMatch
        },
        "sdk2_attributes"       : {
            "name"      : "support.function.component.brightscript",
            "match"     : sdk2AttributesMatch
        },
        "comment"       : {
            "name"      : "comment.line.rem.brightscript",
            "match"     : "^\\s*?(?i:rem\\s).*$\\n?"
        },
        "comment2"       : {
            "captures":{
                "1":{
                    "name": "punctuation.definition.comment.brightscript"
                }
            },
            "name"      : "comment.line.apostrophe.brightscript",
            "match"     : "(').*$\\n?"
        },
        "string"       : {
            "name"      : "string.quoted.double.brightscript",
            "match"     : "\\\"(?:[^\\\"\\\\\\\\]+|\\\\\\\\.)*\\\""
        },
        "class"       : {
            "name"      : "entity.name.brightscript",
            "match"     : "(?i:\\\\b(top|m(.))\\\\b)"
        },
        "methods"       : {
            "name"      : "storage.type.brightscript",
            "match"     : "(?=\\\\.).[^\\\\(\\\\,|\\\\.|\\n|\\\\s|\\\\)]*(?=\\\\()"
        },
        "brackets"      : {
            "name"      : "variable.language.brightscript",
            "match"     : "({|}|:|\\\\[|\\\\])"
        }
    }


writeln(brightScript_cson_file, "patterns: [")
for repo in repositories:
    writeln(brightScript_cson_file, "\t{\n\t\tinclude: \"#"+repo+"\"\n\t}")

writeln(brightScript_cson_file, "]")



writeln(brightScript_tmLanguage_file,
    """\t<key>patterns</key>
\t<array>
\t\t<dict>
\t\t\t<key>match</key>
\t\t\t<string>(').*$\\n?</string>
\t\t\t<key>name</key>
\t\t\t<string>comment.line.apostrophe.brightscript</string>
\t\t</dict>
\t\t<dict>
\t\t\t<key>begin</key>
\t\t\t<string>"</string>
\t\t\t<key>end</key>
\t\t\t<string>"</string>
\t\t\t<key>name</key>
\t\t\t<string>string.quoted.double.brightscript</string>
\t\t</dict>""")


writeln(brightScript_cson_file, "repository:")
for repo in repositories:
    writeln(brightScript_cson_file, "\t"+repo+":")
    # print repo
    writeln(brightScript_tmLanguage_file, "\t\t<dict>")
    for child in repositories[repo]:
        # print child
        # print repositories[repo][child]
        if child == "captures":
            # print child
            n = 3
            # a = repositories[repo][child]
            # for b in a:
                # print a[b]
        else:
            # if child == "match":
            writeln(brightScript_tmLanguage_file, "\t\t\t<key>"+child+"</key>")
                # writeln(brightScript_tmLanguage_file, "\t\t\t<"+child+">"+repositories[repo][child]+"</"+child+">")
            # if child == "name":
                # writeln(brightScript_tmLanguage_file, "\t\t\t<key>name</key>")

            writeln(brightScript_tmLanguage_file, "\t\t\t<string>"+repositories[repo][child].replace("\\\\", "\\")+"</string>")
            writeln(brightScript_cson_file, "\t\t"+child+":\""+repositories[repo][child]+"\"")

    writeln(brightScript_tmLanguage_file, "\t\t</dict>")
        # brightScript_cson_file.write()


# 2


# 2

writeln(brightScript_tmLanguage_file, "\t</array>")

# End for sublime syntax highlight
writeln(brightScript_tmLanguage_file, "</dict>")
writeln(brightScript_tmLanguage_file, "</plist>")


# GENERATE SNIPPETS !!!!
