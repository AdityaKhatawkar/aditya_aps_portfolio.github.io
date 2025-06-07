---
layout: single
title: "CodeNexus"
permalink: /
---

> *Connecting ideas to solutions, one problem at a time!*

<a name="details"></a> 
- **Name:** Aditya N. Khatawkar  
- **SRN:** 01FE22BCS323  
- **Course Name:** Algorithmic Problem Solving   
- **Course Instructor:** Prakash Hegade
- **University:** KLE Technological University, Hubballi
- **Domain:** Youtube

  ---

<a name="about"></a>
## 👨‍💻 About Me
<div class="justified">
  <p>
    I’m <strong>Aditya N. Khatawkar</strong>, currently pursuing a degree in Computer Science and Engineering at KLE Technological University, Hubballi. Passionate about learning, exploring new things, and pushing my boundaries, I’m currently diving deep into <strong>Backend Web Development</strong> and <strong>Data Structures & Algorithms (DSA)</strong>, just trying to live by the quote:
  </p>

  <p>
    <em>"Do what you love, and you'll find people who love what you do."</em>
  </p>
</div>



### 🛠️ Technical Skills

- **Programming Languages:** Python, C, C++
- **Web Development:** HTML, CSS, JavaScript, Node.js, Express.js, Postman  
- **Databases:** MySQL, MongoDB  
- **Version Control:** Git, GitHub  

---

<a name="introduction"></a>
## Introduction
![Google Logo](/assets/images/youtube_logo.png)

<div class="justified">
  <p>
    Founded in 2005 and acquired by Google in 2006, YouTube has evolved from a simple video-sharing site into a massive, data-driven platform that powers content discovery, creator monetization, and user engagement at a global scale. With over <strong>2.7 billion monthly active users</strong> and more than <strong>500 hours of video uploaded every minute</strong>, YouTube operates at an unmatched scale, requiring advanced algorithmic intelligence to manage and optimize operations <a href="#ref1">[1]</a>.
  </p>

  <p>
    In recent years, YouTube has witnessed a massive boom in short-form content with the launch of YouTube Shorts, a feature introduced to compete with TikTok and Instagram Reels. By 2024, YouTube Shorts had surpassed <strong>70 billion daily views</strong> globally <a href="#ref2">[2]</a>. Forrester Research reports that <strong>29% of U.S. Gen Z</strong> online adults now use YouTube Shorts at least weekly, underscoring how bite-sized video is reshaping attention spans and engagement patterns <a href="#ref3">[3]</a>.
  </p>

  <p>
    What makes YouTube unique is not just its scale, but the way it handles business-critical challenges such as content recommendation, ad targeting, trend detection, and moderation. Its backend is deeply rooted in a backbone of data structures and algorithms (DSA). Whether it's ranking the best video for a user, optimizing live video delivery, or filtering spam, YouTube’s success lies in its algorithmic problem-solving capabilities.
  </p>

  <p>
    This portfolio explores YouTube’s real-world business cases and demonstrates how core DSA techniques can be applied to model and solve them efficiently.
  </p>
</div>




### 🏗️ YouTube System Architecture Overview
Having spent hours surfing YouTube every day, I’ve often found myself wondering:
><em>“How does all of this actually work?”</em><br>
><em>“How are videos fetched so efficiently?”</em><br>
><em>“How is such a large amount of content, creator, and viewer data stored?”</em><br>
><em>“Don’t the servers get overloaded with requests? how is that managed?”</em><br>
><em>“How are video bitrates adapted?”</em><br>
><em>“How does the video recommendation work?”</em><br>
><em>“How is content violating DMCA detected?”</em><br>

Below is a concise overview of how YouTube’s core systems handle video from upload through delivery. This high-level architecture lays the groundwork for the business cases we’ll explore next.

![YouTube System Design Architecture](/assets/images/youtube_system_design.png)

*Figure 1: High-level YouTube system design illustrating user upload servers, transcoding clusters, video storage, CDNs, metadata services, and recommendation pipelines.* [4]

<div class="justified">
  <ol>
    <li>
      <strong>User Client → Upload Servers</strong><br />
      <ul>
        <li><strong>Creators</strong> upload raw video files via web or mobile clients.</li>
        <li>Requests pass through a <strong>load balancer</strong> to an <strong>Upload/Web Server</strong>, which writes the file into durable blob storage.</li>
      </ul>
    </li>
    <li>
      <strong>Transcoding & Storage</strong><br />
      <ul>
        <li>A fleet of <strong>Transcoding Servers</strong> retrieves uploads and encodes them into multiple resolutions (144p, 480p, 1080p, etc.).</li>
        <li>Transcoded segments are stored in a distributed <strong>Video Storage</strong> layer; metadata (titles, IDs, thumbnails) is indexed in a <strong>Metadata Store</strong> (e.g., Bigtable, Spanner).</li>
      </ul>
    </li>
    <li>
      <strong>Content Delivery Network (CDN)</strong><br />
      <ul>
        <li>Popular and newly uploaded content is replicated to edge <strong>CDN</strong> nodes worldwide.</li>
        <li>Viewers fetch video chunks from the nearest CDN via adaptive-bitrate protocols (MPEG-DASH, HLS) to minimize latency.</li>
      </ul>
    </li>
    <li>
      <strong>Viewer Playback Path</strong><br />
      <ul>
        <li>A <strong>Viewer</strong> requests a video; the client contacts the closest CDN edge.</li>
        <li>Cache misses trigger a fetch from the origin storage.</li>
        <li><strong>Adaptive streaming algorithms</strong> and <strong>real-time analytics</strong> determine the optimal segment quality.</li>
      </ul>
    </li>
    <li>
      <strong>Metadata & Recommendations</strong><br />
      <ul>
        <li>The client’s API calls hit the <strong>API Server</strong>, which queries the <strong>Metadata Store</strong> for user history and video stats.</li>
        <li><strong>Recommendation engines</strong> (graph-based, collaborative filtering) generate personalized “Up Next” and homepage feeds.</li>
      </ul>
    </li>
  </ol>

  <p>
    This end-to-end pipeline built on load balancers, distributed storage, transcoding clusters, CDNs, and recommendation services forms the foundation for all the business-critical scenarios in this portfolio. In the sections that follow, we’ll dive into specific cases and show how Data Structures & Algorithms (DSA) techniques solve them efficiently.
  </p>
</div>

<a name="cases"></a>
## 💼 Business Cases
### I. Content Delivery and Infrastructure

YouTube’s backend must handle uploading, transcoding, storage, and streaming to millions of devices. The key is fast retrieval and minimal latency. Services are replicated across regions, and popular content is pushed to edge servers (CDNs) [5]. Efficient algorithms are used for routing, load balancing, and data placement.

#### 1. Content Delivery Network (CDN) Server Selection
When serving a video stream, YouTube must select the nearest CDN edge server or region to minimize latency. Given a user’s geographic location, we want the closest server.

**Algorithm:** KD-Tree Nearest-Neighbor Search

<a href="./01.html" class="button">More ▶️</a>

#### 2. Shortest-Path Routing in CDN Network
Once YouTube selects a CDN edge region to serve the user, the system must determine how to route the request through the network to that destination with minimal latency.

**Algorithm:** A* Graph Search

<a href="./02.html" class="button">More ▶️</a>

#### 3. Content Delivery Network (CDN) Optimization
To ensure YouTube’s video content reaches users quickly and reliably, Google must optimize the underlying physical network that connects data centers, edge servers, and backbone links.

**Algorithm:** Borůvka’s Algorithm for Minimum Spanning Tree (MST)

<a href="./03.html" class="button">More ▶️</a>

---

<a name="references"></a>
### References

1. Statista. *Most popular social networks worldwide as of February 2025, by number of monthly active users*.  
   Available at: [https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/](https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/)

2. Grin. *The Rise of YouTube Shorts*.  
   Available at: [https://grin.co/blog/youtube-shorts-in-influencer-marketing/](https://grin.co/blog/youtube-shorts-in-influencer-marketing/)

3. Forrester. *Meta’s Short-Form Video Strategy Isn’t Reeling In Market Share*.  
   Available at: [https://www.forrester.com/blogs/metas-short-form-video-strategy-isnt-reeling-in-market-share/](https://www.forrester.com/blogs/metas-short-form-video-strategy-isnt-reeling-in-market-share/)

4. GeeksforGeeks. *System Design of Youtube - A Complete Architecture*.
   Available at: [https://www.geeksforgeeks.org/system-design-of-youtube-a-complete-architecture/](https://www.geeksforgeeks.org/system-design-of-youtube-a-complete-architecture/)

5. Dev.to. *System Design of YouTube: A Detailed Deep Dive into the Video Giant*
   Available at: [https://dev.to/wittedtech-by-harshit/system-design-of-youtube-a-detailed-deep-dive-into-the-video-giant-5019](https://dev.to/wittedtech-by-harshit/system-design-of-youtube-a-detailed-deep-dive-into-the-video-giant-5019)

