using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class clickableObject : MonoBehaviour
{
    private Button objectButton;

    //name of scene to load as to be set in the inspector
    public string nameSceneToLoad;

    void Start()
    {
        //find the button attach to the image
        objectButton = transform.gameObject.GetComponent<Button>();
        //wait for click event on the button
        objectButton.onClick.AddListener(() => ButtonClicked());
    }

    void ButtonClicked()
    {
        //Output this to console when the Button is clicked
        Debug.Log(transform.gameObject.name + " has been clicked");
        //Load the specific scene
        SceneManager.LoadScene("Cofee", LoadSceneMode.Additive);
    }

}
