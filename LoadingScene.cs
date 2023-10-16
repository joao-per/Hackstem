using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.SceneManagement;

public class LoadingScene : MonoBehaviour
{
    public Slider loadingBar;
    public TextMeshProUGUI curiosityText;
    public TextMeshProUGUI percentageText;
    private string[] curiosities = {
        "Did you know that rising global temperatures threaten cocoa production? In a few decades, that delicious chocolate bar could be a rare treat!",
        "Did you know that the fashion industry is the second-largest polluter in the world after the oil industry? Your choices in clothing can make a big difference!",
        "Did you know that although coral reefs cover less than 1% of the Earth's surface, they provide a home for 25% of all marine species? It's like a bustling city underwater!",
        "Did you know that the average person eats 70,000 microplastics each year? That's like eating a credit card every week!",
        "Did you know that the average person uses 150 litres of water per day? That's like 300 bottles of water!",
        "Did you know that if the Greenland ice sheet melted entirely, global sea levels would rise by about 20 feet? That's taller than a giraffe!",
        "You can save 2,400 litres of water a month by turning off the tap while brushing your teeth!",
        "You won't believe this, but the average person uses 13,000 plastic bottles in their lifetime! That's enough to build a bridge from London to New York!",
        "Did you know that the majority of icebergs are made from freshwater? If you melted an average-sized iceberg, it could provide drinking water for half a million people for a year!",
        "Did you know that bees pollinate roughly 70% of the world's crops? Without them, our diet would be severely limited!",
        "Did you know that shade-grown coffee farms provide crucial habitats for many bird species? So, choosing shade-grown coffee helps both your morning routine and the birds!",

    };
    private string nextSceneName = "Main"; // The name of your main scene

    private float fakeLoadingSpeed = 0.2f; // You can adjust this to control how fast the bar fills up
    private float currentProgress = 0.0f;

    private void Start()
    {
        // Choose a random curiosity
        curiosityText.text = curiosities[Random.Range(0, curiosities.Length)];
        
        // Start the fake loading
        StartCoroutine(FakeLoading());
    }

    private IEnumerator FakeLoading()
    {
        while (currentProgress < 1.0f)
        {
            currentProgress += fakeLoadingSpeed * Time.deltaTime;
            loadingBar.value = currentProgress;
            percentageText.text = $"{(int)(currentProgress * 100)}%"; 
            yield return null;
        }

        // Once our fake loading is done, actually load the next scene.
        SceneManager.LoadScene(nextSceneName);
    }
}
