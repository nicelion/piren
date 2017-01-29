#!/bin/bash

whiptail --title 'piren-config' --msgbox "Welcome to piren-config. Using this script, you can easily add new horns and create presets for piren use. You can also configure pin settings, among other settigns. \n\n\n\nClick return to continue." 20 60

# if (whiptail --title "Test Yes/No Box" --yesno "Choose between Yes and No." 10 60) then
#     echo "You chose Yes. Exit status was $?."
# else
#     echo "You chose No. Exit status was $?."
# fi

# if (whiptail --title "Test Yes/No Box" --yes-button "Skittles" --no-button "M&M's"  --yesno "Which do you like better?" 10 60) then
#     echo "You chose Skittles Exit status was $?."
# else
#     echo "You chose M&M's. Exit status was $?."
# fi


# PET=$(whiptail --title "Test Free-form Input Box" --inputbox "What is your pet's name?" 10 60 3>&1 1>&2 2>&3)
 
# exitstatus=$?
# if [ $exitstatus = 0 ]; then
#     echo "Your pet name is:" $PET
# else
#     echo "You chose Cancel."
# fi

OPTION=$(whiptail --title "piren-config menu" --menu "Choose your option" 15 60 5 \
"1" "Add Siren" \
"2" "Add Horn" \
"3" "Add Preset" \
"4" "Change Pins" \
"5" "Licence" 3>&1 1>&2 2>&3)
 
re='^[0-9]+$'

exitstatus=$?
if [ $exitstatus = 0 ]; then
    if [ $OPTION == 4 ]; then
    	PIN_OPTION=$(whiptail --title "Change Pins" --menu "Choose Pin to Change" 15 60 5 \
			"1" "Manual Wail" \
			"2" "Horn" \
			"3" "Phaser" \
			"4" "Yelp" \
			"5" "Wail Loop" 3>&1 1>&2 2>&3)
		


		if [ $PIN_OPTION == 1 ]; then

			WAIL_PIN=$(whiptail --title "Manual Wail Pin" --inputbox "What would you like to change the wail pin to" 10 60 25 3>&1 1>&2 2>&3)
			if [ $exitstatus = 0 ]; then
			    echo "Attempting to change wail pin to " $WAIL_PIN
			    echo "Verifing.........."

			    if ! [ $WAIL_PIN =~ $re ]; then 
			    	   echo "error: Not a number" >&2; exit 1
			    fi
			else
			    echo "You chose Cancel."
			fi
		fi
    fi


else
    echo "You chose Cancel."
fi
