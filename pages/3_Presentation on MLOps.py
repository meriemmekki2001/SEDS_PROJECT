import streamlit as st
import reveal_slides as rs

sample_markdown = r"""
# <h1 style="color: #faa937;">  MLOps <h1>
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
--
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
<p> Machine Learning Operations involves a set of processes or rather a sequence of steps implemented to deploy an ML model to the production environment. </p>
<p> There are several steps to be undertaken before an ML Model is production-ready. These processes ensure that your model can be scaled for a large user base and perform accurately. </p>

---
##  <h3 style="color: #faa937;"> Why do we need MLOps? <h3>
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
- ML models rely on a huge amount of data, difficult for a single person to keep track of. <!-- .element: class="fragment" data-fragment-index="0" -->
- Difficult to keep track of parameters we tweak in ML models. Small changes can lead to enormous differences in the results.<!-- .element: class="fragment" data-fragment-index="1" -->
- We have to keep track of the features the model works with, feature engineering is a separate task that contributes largely to model accuracy.<!-- .element: class="fragment" data-fragment-index="2" -->
- Monitoring an ML model isn’t like monitoring a deployed software or web app. <!-- .element: class="fragment" data-fragment-index="3" -->
- Models rely on real-world data for predicting, as real-world data changes, so should the model. This means we have to keep track of new data changes and make sure the model learns accordingly. <!-- .element: class="fragment" data-fragment-index="4" -->
---
## <h3 style="color: #faa937;"> DevOps vs MLOps <h3> 
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
DevOps is a broader approach that spans software development and IT operations for traditional applications, MLOps is a specialized extension of DevOps tailored to the needs of machine learning systems.
---
## <h3 style="color: #faa937;"> ML Project Lifecycle <h3> 
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
- Scoping  <!-- .element: class="fragment" data-fragment-index="0" -->
- Data Engineering <!-- .element: class="fragment" data-fragment-index="1" -->
- Modelling .<!-- .element: class="fragment" data-fragment-index="2" -->
- Deployment <!-- .element: class="fragment" data-fragment-index="3" -->
- Monitoring <!-- .element: class="fragment" data-fragment-index="4" -->
---

##  <h3 style="color: #faa937;"> ML Production Infrastructure <h3> 
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
- Data Collection  <!-- .element: class="fragment" data-fragment-index="0" -->
- Data Verification <!-- .element: class="fragment" data-fragment-index="1" -->
- Feature Extraction  .<!-- .element: class="fragment" data-fragment-index="2" -->
- Configuration <!-- .element: class="fragment" data-fragment-index="3" -->
- ML Code  <!-- .element: class="fragment" data-fragment-index="4" -->  
- Machine Resource Management  <!-- .element: class="fragment" data-fragment-index="5" -->  
- Analysis Tool  <!-- .element: class="fragment" data-fragment-index="6" --> 
-  Project Management Tool  <!-- .element: class="fragment" data-fragment-index="7" --> 
- Serving Infrastructure  <!-- .element: class="fragment" data-fragment-index="8" --> 
-  Monitoring   <!-- .element: class="fragment" data-fragment-index="9" --> 
---
## <h2 style="color: #faa937;"> Thank You for Listening <h2> 
<!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
Any questions ?
"""
st.markdown("")                 
currState = rs.slides(sample_markdown, 
                    height=700, 
                    theme='night', 
                    config={
                            "width": 900, 
                            "height": 900, 
                            "minScale": 0.0, 
                            "center": True, 
                            "maxScale": 5.0, 
                            "margin": 0.1,

                            }, 
                  
                    markdown_props={"data-separator-vertical":"^--$"}, 
                    key="foo")
