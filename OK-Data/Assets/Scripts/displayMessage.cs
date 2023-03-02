using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class displayMessage : MonoBehaviour
{
    public GameObject newGameObject;
    public Transform parent;
    public TMP_Text messageContent;
    public Sprite[] profilePictures;


    void Start()
    {
        //debug start by displaying two messages and destroy the inspector one
        InstantiateMessage("test", true,true); //Display a test message
        InstantiateMessage("Ceci est un autre texte", false,false); //Display a test message
        destroyMessages(1); //Destroy index X message, if value 0 then destroy all messages
    }

//Fonction to display message on smartphone screen
//Message = text content
//qActive = display a yes/no answer
//medTalk = message coming from mediateur or not
    public void InstantiateMessage(string message, bool qActive, bool medTalk)
    {
        newGameObject.SetActive(true);
        Transform YesNo = transform.GetChild(1).GetChild(1); //find yes no element
        YesNo.gameObject.SetActive(qActive); //Display or not yes no question
        messageContent.SetText(message); //Set message to display
        Instantiate(newGameObject, parent, messageContent);

        //Change aesthetics message display depend of sender
        Transform background = transform.GetChild(1);
        Transform colorText = background.GetChild(0).GetChild(1);
        Debug.Log(background);
        if(medTalk){
            Debug.Log("le mediateur parle");
            background.GetComponent<Image>().color = new Color32(0,0,0,225);
            colorText.GetComponent<TextMeshProUGUI>().color = new Color32(255,255,255,255);
            ChangeSprite(0);

        }
        else
        {
            Debug.Log("quelqu'un d'autre parle");
            background.GetComponent<Image>().color = new Color32(255,255,225,100);
            colorText.GetComponent<TextMeshProUGUI>().color = new Color32(0,0,0,255);
            ChangeSprite(1);
        }
    }

//Change Icon from text message
    void ChangeSprite(int index) 
    { 
        //Check index value link to profile picture in editor
        Transform profilePicture = transform.GetChild(1).GetChild(0).GetChild(0);
        profilePicture.GetComponent<Image>().sprite = profilePictures[index]; 
    }

//Destroy message display
//Index = how many message should be destroy from older one to new one
//if index = 0, all messages will be destroy
    public void destroyMessages(int index){
        int numberChildren = transform.childCount-1;
        if(index==0){
            for(int i = 1; i <= numberChildren; i++)
            {
                Destroy(transform.GetChild(i).gameObject);
            }
        } else {
            Destroy(transform.GetChild(index).gameObject);
        }
    }

//Display image in smartphone
    public void InstantiateImage(){

    }
}
