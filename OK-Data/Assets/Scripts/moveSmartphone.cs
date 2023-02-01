using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class moveSmartphone : MonoBehaviour
{
    public Button moveButton;
    public GameObject smartPhoneObject;
    public int endPosition;
    public float timeTween;
    bool upPhone = true;
    float initPosY;

    void Start()
    {
        //wait for click event on MovePhoneButton and launc MovingSmartphone function
        moveButton.onClick.AddListener(MovingSmartphone);

        //set the init pose smartphone as the default one (in display mode)
        // → tansform position return always a positive value even if it's negatvie
        // → artificially negative position by adding "-"
        initPosY = -transform.position.y;
        Debug.Log("Position Y : " + initPosY);
    }


    public void MovingSmartphone()
    {
        //easeIn allow us to move smartphone in a smooth transition
        //If we want to change this smooth :
        //Type of easeIn on easeings.net

        Debug.Log("actual position is : " + transform.position.y);
        if(upPhone)
        {
            LeanTween.moveY(smartPhoneObject.GetComponent<RectTransform>(),endPosition,timeTween).setEase(LeanTweenType.easeOutQuart);
            upPhone = !upPhone;  
            //Debug.Log(upPhone);
        } 
        else 
        {
            LeanTween.moveY(smartPhoneObject.GetComponent<RectTransform>(),initPosY,timeTween).setEase(LeanTweenType.easeOutBack);
            upPhone = !upPhone;  
            //Debug.Log(upPhone); 
        }
    }
}
