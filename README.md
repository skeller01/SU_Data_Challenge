# syracuse_data_challenge
https://data.syr.gov/pages/data-challenge

# The Seven Bridges of Königsberg and Finding Public Art in Syracuse
<iframe src="syracuse_route.html"
        width="100%"
        height="500"
        style="border:none;"></iframe>

## Introduction

The Seven Bridges of Königsberg is a classic problem in mathematics that asks whether it is possible to walk through all the seven bridges in the city without repeating any. The problem was solved by Euler, who proved that it was impossible. In this project, we are applying the same concept to finding the shortest path to all of the public art in the city of Syracuse.

## Problem Statement

Syracuse is a city in upstate New York with a rich history and vibrant arts scene. The city has public works of art, including sculptures, murals, and installations. Our task is to find the shortest path to visit all of these public art pieces without repeating any and to also show nearby restaurants. 

## Approach

### Google API for Places and Maps 
![Alt Text](/images/Google_API_ETL.png)

###
We can model the problem by creating a graph where the nodes represent the public art pieces and the edges represent the distance between them. We can then use graph traversal algorithms to find the shortest path that visits all of the nodes without repeating.

To obtain the data for the graph, we will use the Google Places API (PlacesAPI.py) to retrieve the google places_id of the public art pieces. Next, we could use google's map API with waypoints to calculate the optimized traveling path. In this case we just wrote a basic algorithm to help calculate the optimal path.(optimal.py)

In addition to finding the shortest path to the public art, we will also use the Google Places API to find the closest restaurant to each art piece. We can then display the entire route on a map using a library like folium. (visualize.py)

## Discussion 
We didn't have the time to complete this project beyond a proof of concept but we leave the code open source so anyone can try and improve. We believe you could divide the city into sectors and then run optimization to find the fastest route anchored around areas of the city you could walk to the art. You could then turn this into an online brochure advertising hotels and restaurants in those areas or places to grab a coffee while you walk and enjoy the art! 

## Conclusion

The Seven Bridges of Königsberg problem provided a foundational concept for graph theory, which has numerous practical applications in computer science and engineering. By applying this concept to finding the shortest path to all of the public art in Syracuse, we can create a useful tool for art enthusiasts and tourists alike.