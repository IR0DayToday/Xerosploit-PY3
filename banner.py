#!/usr/bin/python
# -*- coding: utf-8 -*-
# Xerosploit banners


#---------------------------------------------------------------------------#
# This file is part of Xerosploit.                                          #
# Xerosploit is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# Xerosploit is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with Xerosploit.                                                    #
# If not, see <http://www.github.com/IR0DAYTODAY/XEROSPLOIT/licenses/>.     #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#        Copyright © 2021 By IR0Day.Today Bax (t.me/LearnXPLOIT)            #
#                                                                           #
#---------------------------------------------------------------------------#


import random

header1 = """  

▒██   ██▒▓█████  ██▀███   ▒█████    ██████  ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
▒▒ █ █ ▒░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
░░  █   ░▒███   ▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
 ░ █ █ ▒ ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░  ▒   ██▒▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
▒██▒ ▒██▒░▒████▒░██▓ ▒██▒░ ████▓▒░▒██████▒▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
░░   ░▒ ░ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
 ░    ░     ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
 ░    ░     ░  ░   ░         ░ ░        ░               ░  ░    ░ ░   ░           
"""

header2 = """

██╗  ██╗███████╗██████╗  ██████╗ ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
╚██╗██╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
 ╚███╔╝ █████╗  ██████╔╝██║   ██║███████╗██████╔╝██║     ██║   ██║██║   ██║   
 ██╔██╗ ██╔══╝  ██╔══██╗██║   ██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
██╔╝ ██╗███████╗██║  ██║╚██████╔╝███████║██║     ███████╗╚██████╔╝██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝                                                      
"""

header3 = """

        ▄  ▄███▄   █▄▄▄▄ ████▄    ▄▄▄▄▄   █ ▄▄  █     ████▄ ▄█    ▄▄▄▄▀ 
    ▀▄   █ █▀   ▀  █  ▄▀ █   █   █     ▀▄ █   █ █     █   █ ██ ▀▀▀ █    
      █ ▀  ██▄▄    █▀▀▌  █   █ ▄  ▀▀▀▀▄   █▀▀▀  █     █   █ ██     █    
     ▄ █   █▄   ▄▀ █  █  ▀████  ▀▄▄▄▄▀    █     ███▄  ▀████ ▐█    █     
    █   ▀▄ ▀███▀     █                     █        ▀        ▐   ▀      
     ▀              ▀                       ▀                           
"""

header4 = """
____  __                     \033[1;36m________         ______       _____ _____ \033[1;m
__  |/ /_____ ______________ \033[1;36m__  ___/________ ___  /______ ___(_)__  /_\033[1;m
__    / _  _ \__  ___/_  __ \\\033[1;36m_____ \ ___  __ \__  / _  __ \__  / _  __/\033[1;m
_    |  /  __/_  /    / /_/ /\033[1;36m____/ / __  /_/ /_  /  / /_/ /_  /  / /_  \033[1;m
/_/|_|  \___/ /_/     \____/ \033[1;36m/____/  _  .___/ /_/   \____/ /_/   \__/  \033[1;m
                             \033[1;36m        /_/                               \033[1;m     
"""

header5 = """
               \u001b[31my▄╓╓╓|,,,,                                ,,,|y╓╓▄▄

               \u001b[31m└╙▓▒▓▓▓▓▒░M###╔╔╔╓,,            ,,╓╔╔####░▒▒▓▓▓▓▒▓∩

                \u001b[31m└╙▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░M,        |#▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒∩

                 \u001b[31m└╙▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓░∩     |{▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒┘

                    \u001b[31m└└╙▀▓█▓▓▓▓▓▓▓▓▓▒▓N     └╫▓▒▓▓▓▓▓▓▓▓▓█▀▒╙└

                        \u001b[31m└└╙╙╙▒▒▒╙╙╙└         └└╙╙▒▒▒▒╙╙╙└└

                   \u001b[31m▓╔.                                       ƒ

                   \u001b[31m╫║╖║ ..                              «  └▓

                    \u001b[31m" % █ └ Kⁿ¬                   ┌∞^% (▄▓  ╙

                         \u001b[31m½é ▌  ▓ å╙  ¥ à  ""Ñ ╓Ö ▓▐  å ∩

                              \u001b[31m" 4- ▀  ║    (b ╙╖«╜└"

			          \u001b[34mIR0Day.Today Bax
			          \u001b[32mt.me/LearnExploit
 		\u001b[33mnew version for kali linux V 2021.x [tested on kalilinux 2021.3]\u001b[0m

"""

def xe_header():
	headers = header5
	return headers
    #headers = [header5, header2]
    #return random.choice(headers)
