using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class clickableObject : MonoBehaviour
{
    private Button objectButton;
    public string nameSceneToLoad;
    // Start is called before the first frame update
    void Start()
    {
        objectButton = transform.gameObject.GetComponent<Button>();
        objectButton.onClick.AddListener(() => ButtonClicked());
    }

    void ButtonClicked()
    {
        //Output this to console when the Button3 is clicked
        Debug.Log(transform.gameObject.name + " has been clicked");
        SceneManager.LoadScene(nameSceneToLoad, LoadSceneMode.Additive);
    }
}
