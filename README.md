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

<div class="justified">
  <p>
    Below is a concise overview of how YouTube’s core systems handle video from upload through delivery. This high-level architecture lays the groundwork for the business cases we’ll explore next.
  </p>
</div>

![YouTube System Design Architecture](/assets/images/youtube_system_design.png)

<div class="justified" style="margin-top: 1em;">
  <em>Figure 1: High-level YouTube system design illustrating user upload servers, transcoding clusters, video storage, CDNs, metadata services, and recommendation pipelines.</em> [4]
</div>

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

### I. Ingestion & Storage

#### 1. Optimal Video Upload Scheduling  
<p class="justified">We split a creator’s large video into chunks and schedule parallel uploads to regional servers. A dynamic-programming planner weighs chunk sizes against server load and network delays ensuring fast, balanced ingestion.</p>  
**Design Technique / Algorithm:** Dynamic Programming<br>  
<a href="./01.html" class="button">More ▶️</a>

#### 2. Copyright Fingerprint Scanning  
<p class="justified">As chunks arrive, we immediately fingerprint them with a rolling-hash (Rabin–Karp) to catch potential infringements before storage. Early detection prevents unauthorized content from ever entering our repository.</p>  
**Design Technique / Algorithm:** Rabin–Karp Rolling Hash<br>  
<a href="./02.html" class="button">More ▶️</a>

#### 3. Storage-Aware Server Assignment  
<p class="justified">Approved video chunks are mapped to storage nodes via consistent hashing. This evenly distributes load and minimizes reshuffling when capacity changes, locking in a stable foundation for delivery and caching.</p>  
**Design Technique / Algorithm:** Consistent Hashing<br>  
<a href="./03.html" class="button">More ▶️</a>

---

### II. Content Delivery & Optimization

#### 4. CDN Edge Server Selection  
<p class="justified">Given a viewer’s location, we query a KD-Tree of edge servers to pick the nearest node. This decision layer ensures each playback starts from the lowest-latency edge.</p>  
**Design Technique / Algorithm:** KD-Tree Nearest-Neighbor Search<br>  
<a href="./04.html" class="button">More ▶️</a>

#### 5. Shortest-Path Routing  
<p class="justified">Once an edge is chosen, an A* search over our backbone graph computes the fastest network path, navigating around congestion or outages to maintain consistent throughput.</p>  
**Design Technique / Algorithm:** A* Graph Search<br>  
<a href="./05.html" class="button">More ▶️</a>

#### 6. CDN Network Optimization  
<p class="justified">Periodically, we rebuild the minimum spanning tree of data centers and edges using Borůvka’s algorithm. This reveals the most cost-efficient set of physical links, ensuring our backbone remains lean and resilient.</p>  
**Design Technique / Algorithm:** Borůvka’s Algorithm for MST<br>  
<a href="./06.html" class="button">More ▶️</a>

#### 7. Load Balancing  
<p class="justified">To handle unpredictable demand, incoming streams are distributed across server pools in a Round-Robin fashion augmented with real-time health checks preventing hot spots during viral peaks.</p>  
**Design Technique / Algorithm:** Round Robin<br>  
<a href="./07.html" class="button">More ▶️</a>

#### 8. Adaptive Bitrate Delivery  
<p class="justified">As playback begins, we break the video into quality-graded segments. A knapsack-style DP selects the highest bitrate that fits current bandwidth and buffer targets dynamically swapping streams to avoid rebuffering.</p>  
**Design Technique / Algorithm:** Dynamic Programming (Knapsack)<br>  
<a href="./08.html" class="button">More ▶️</a>

#### 9. CDN Caching & Eviction  
<p class="justified">Popular content lives in edge caches. We run an LRU eviction policy so that only recent high-demand videos remain close to users feeding back into future edge-selection decisions.</p>  
**Design Technique / Algorithm:** LRU Cache Policy<br>  
<a href="./09.html" class="button">More ▶️</a>

---

### III. Discovery & Filtering

#### 10. Real-Time Metrics Aggregation  
<p class="justified">Every view, like, and comment fires an event. We use Fenwick trees for log-time updates and prefix queries, powering live dashboards and trend-detection triggers.</p>  
**Design Technique / Algorithm:** Fenwick Tree<br>  
<a href="./10.html" class="button">More ▶️</a>

#### 11. Trending Query Detection  
<p class="justified">Mo’s algorithm scans sliding time windows over our search logs to spot surges in specific terms, fueling “hot” search suggestions and surfacing emerging interests.</p>  
**Design Technique / Algorithm:** Mo’s Algorithm<br>  
<a href="./11.html" class="button">More ▶️</a>

#### 12. Autocomplete Search Suggestions  
<p class="justified">As users type, a Trie of historical queries delivers instant prefix matches, reducing keystrokes and guiding them toward popular searches.</p>  
**Design Technique / Algorithm:** Trie<br>  
<a href="./12.html" class="button">More ▶️</a>

#### 13. Search Spell Correction  
<p class="justified">When users mistype, we combine Trie lookups with edit-distance calculations to suggest the closest valid queries, minimizing zero-result searches and keeping users on track.</p>  
**Design Technique / Algorithm:** Trie + Edit Distance<br>  
<a href="./13.html" class="button">More ▶️</a>

#### 14. Spam Comment Filtering  
<p class="justified">Incoming comments are first checked against a Bloom filter of banned phrases. Suspects get escalated to deeper NLP checks, keeping abuse rates low without slowing down posting.</p>  
**Design Technique / Algorithm:** Bloom Filter<br>  
<a href="./14.html" class="button">More ▶️</a>

#### 15. User Profiling & Segmentation  
<p class="justified">We cluster viewers by watch patterns and engagement behaviors using Union-Find on a similarity graph. These segments feed personalized search rankings and targeted recommendation models.</p>  
**Design Technique / Algorithm:** Union-Find<br>  
<a href="./15.html" class="button">More ▶️</a>

---

### IV. Recommendation & Engagement

#### 16. Collaborative Filtering  
<p class="justified">For each user segment, we build a user–item matrix and apply matrix factorization to suggest videos that “peers” in their cluster enjoyed, lifting watch time and session depth.</p>  
**Design Technique / Algorithm:** Collaborative Filtering<br>  
<a href="./16.html" class="button">More ▶️</a>

#### 17. Video Importance Ranking  
<p class="justified">We model user transitions between videos as a directed graph and run PageRank to score each video’s stickiness. These scores adjust both home-page carousels and “Up Next” feeds.</p>  
**Design Technique / Algorithm:** PageRank<br>  
<a href="./17.html" class="button">More ▶️</a>

#### 18. Common Category Detection  
<p class="justified">To suggest relevant tags or playlists, we compute the least common ancestor in our category hierarchy via binary lifting, finding the most specific shared genre among related videos or channels.</p>  
**Design Technique / Algorithm:** Binary Lifting for LCA<br>  
<a href="./18.html" class="button">More ▶️</a>

#### 19. Fair Playlist Shuffle  
<p class="justified">Within any playlist, the Johnson–Trotter algorithm generates a full permutation sequence before repeating, guaranteeing each video appears once per cycle and avoiding unintended bias.</p>  
**Design Technique / Algorithm:** Johnson–Trotter Algorithm<br>  
<a href="./19.html" class="button">More ▶️</a>

---

### V. Monetization & Optimization

#### 20. Ad Placement Scheduling  
<p class="justified">We model ad slots as edges in a flow network: Ford-Fulkerson max-flow finds the optimal allocation of ad segments across videos and user cohorts, balancing revenue with viewer experience.</p>  
**Design Technique / Algorithm:** Ford-Fulkerson Algorithm<br>  
<a href="./20.html" class="button">More ▶️</a>

#### 21. Real-Time Ad Auction  
<p class="justified">For each slot, advertisers bid in a Vickrey (second-price) auction. Our MVC pipeline judges bids in parallel, picking the winner and charging the runner-up price, optimizing fairness and RPM.</p>  
**Design Technique / Algorithm:** Vickrey Auction + MVC Architecture<br>  
<a href="./21.html" class="button">More ▶️</a>

#### 22. Dynamic Ad Sequencing  
<p class="justified">For long-form content, dynamic programming schedules multiple ads maximizing total revenue while capping insertions so as not to exceed viewer tolerance thresholds.</p>  
**Design Technique / Algorithm:** Dynamic Programming<br>  
<a href="./22.html" class="button">More ▶️</a>

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

