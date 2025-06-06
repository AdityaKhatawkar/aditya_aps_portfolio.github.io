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
I’m **Aditya N. Khatawkar**, currently pursuing a degree in Computer Science and Engineering at KLE Technological University, Hubballi. Passionate about learning, exploring new things, and pushing my boundaries, I’m currently diving deep into **Backend Web Development** and **Data Structures & Algorithms (DSA)** — just trying to live by the quote:  
*"Do what you love, and you'll find people who love what you do"* .



### 🛠️ Technical Skills

- **Programming Languages:** Python, C, C++
- **Web Development:** HTML, CSS, JavaScript, Node.js, Express.js, Postman  
- **Databases:** MySQL, MongoDB  
- **Version Control:** Git, GitHub  

---

<a name="introduction"></a>
## Introduction
![Google Logo](/assets/images/youtube_logo.png)

Founded in 2005 and acquired by Google in 2006, YouTube has evolved from a simple video-sharing site into a massive, data-driven platform that powers content discovery, creator monetization, and user engagement at a global scale. With over 2.7 billion monthly active users and more than 500 hours of video uploaded every minute, YouTube operates at an unmatched scale, requiring advanced algorithmic intelligence to manage and optimize operations [1]. In recent years, YouTube has witnessed a massive boom in short-form content with the launch of YouTube Shorts, a feature introduced to compete with TikTok and Instagram Reels. By 2024, YouTube Shorts had surpassed 70 billion daily views globally [2]. Forrester Research reports that 29% of U.S. Gen Z online adults now use YouTube Shorts at least weekly—underscoring how bite-sized video is reshaping attention spans and engagement patterns [3].

What makes YouTube unique is not just its scale, but the way it handles business-critical challenges such as, content recommendation, ad targeting, trend detection, and moderation, usingis deeply rooted a backbone of data structures and algorithms (DSA). Whether it's ranking the best video for a user, optimizing live video delivery, or filtering spam, YouTube’s success  in algorithmic problem-solving.

This portfolio explores YouTube’s real-world business cases and demonstrates how core DSA techniques can be applied to model and solve them efficiently.



### 🏗️ YouTube System Architecture Overview
Having spent hours surfing YouTube every day, I’ve often found myself wondering:
<div style="background-color: #f5f5f5; border-left: 4px solid #007BFF; padding: 12px; margin-bottom: 1em;">
  <em>“How does all of this actually work?”</em><br>
  <em>“How are videos fetched so efficiently?”</em><br>
  <em>“How is such a large amount of content, creator, and viewer data stored?”</em><br>
  <em>“Don’t the servers get overloaded with requests—how is that managed?”</em><br>
  <em>“How are video bitrates adapted?”</em><br>
  <em>“How does the video recommendation work?”</em><br>
  <em>“How is content violating DMCA detected?”</em><br><br>
</div>
These and other similar questions always seem to loom in my mind.

 

Below is a concise overview of how YouTube’s core systems handle video from upload through delivery. This high-level architecture lays the groundwork for the business cases we’ll explore next.

![YouTube System Design Architecture](/assets/images/youtube_system_design.png)

*Figure 1: High-level YouTube system design illustrating user upload servers, transcoding clusters, video storage, CDNs, metadata services, and recommendation pipelines.* [4]

1. **User Client → Upload Servers**  
   - **Creators** upload raw video files via web or mobile clients.  
   - Requests pass through a **load balancer** to an **Upload/Web Server**, which writes the file into durable blob storage.

2. **Transcoding & Storage**  
   - A fleet of **Transcoding Servers** retrieves uploads and encodes them into multiple resolutions (144p, 480p, 1080p, etc.).  
   - Transcoded segments are stored in a distributed **Video Storage** layer; metadata (titles, IDs, thumbnails) is indexed in a **Metadata Store** (e.g., Bigtable, Spanner).

3. **Content Delivery Network (CDN)**  
   - Popular and newly uploaded content is replicated to edge **CDN** nodes worldwide.  
   - Viewers fetch video chunks from the nearest CDN via adaptive-bitrate protocols (MPEG-DASH, HLS) to minimize latency.

4. **Viewer Playback Path**  
   - A **Viewer** requests a video; the client contacts the closest CDN edge.  
   - Cache misses trigger a fetch from the origin storage.  
   - **Adaptive streaming algorithms** and **real-time analytics** determine the optimal segment quality.

5. **Metadata & Recommendations**  
   - Meanwhile, the client’s API calls hit the **API Server**, which queries the **Metadata Store** for user history and video stats.  
   - **Recommendation engines** (graph-based, collaborative filtering) generate personalized “Up Next” and homepage feeds.

---

This end-to-end pipeline—built on load balancers, distributed storage, transcoding clusters, CDNs, and recommendation services—forms the foundation for all the business-critical scenarios in this portfolio. In the sections that follow, we’ll dive into specific cases and show how Data Structures & Algorithms (DSA) techniques solve them efficiently.

---

<a name="cases"></a>
## 💼 Business Cases
### 1. YouTube Video Comments Management

Managing the vast number of comments on YouTube videos requires intelligent systems to filter spam, detect toxicity, and highlight meaningful interactions. This business case explores how backend systems and algorithms can improve user engagement and maintain community standards.

### 2. YouTube Copyright Infringement Detection

With millions of videos uploaded daily, YouTube faces the challenge of identifying copyrighted content in real-time. This business case focuses on how data structures, pattern matching, and scalable backend systems can help detect and handle copyright violations efficiently.

### 3. Cost-Optimized Resource Allocation in Google Cloud billing

Google Cloud dynamically allocates resources based on cost and performance constraints. This problem can be modeled using **DP (Knapsack-like problems)** where the goal is to maximize resource usage within a cost or performance budget.


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



