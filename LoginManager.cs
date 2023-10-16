using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;
using UnityEngine.UI;
using System.Collections;
using TMPro;

public class LoginManager : MonoBehaviour
{

	public TMP_InputField usernameField;
	public TMP_InputField passwordField;
	public GameObject popup;
	public TMP_Text popupText;
	
	private string apiUrl = "http://127.0.0.1:5000/teste";
	
	public void Login()
	{
		string username = usernameField.text;
		string password = passwordField.text;

		StartCoroutine(LoginCoroutine(username, password));
	}

	private IEnumerator LoginCoroutine(string username, string password)
	{
		WWWForm form = new WWWForm();
		form.AddField("username", username);
		form.AddField("password", password);

		using (UnityWebRequest www = UnityWebRequest.Post(apiUrl, form))
		{
			yield return www.SendWebRequest();

			/* if (www.result != UnityWebRequest.Result.Success)
			{
				Debug.Log(www.error);
				ShowPopup("Dados de Login incorretos");
			}
			else
			{
				Debug.Log("Login bem-sucedido!"); */
				SceneManager.LoadScene("Loading");
			/* } */
		}
	}

	private void ShowPopup(string message)
	{
		popupText.text = message;
		popup.SetActive(true);
		//wait 5 seconds and hide popup
		StartCoroutine(HidePopup());
	}

	private IEnumerator HidePopup()
	{
		yield return new WaitForSeconds(2);
		popup.SetActive(false);
	}
}
