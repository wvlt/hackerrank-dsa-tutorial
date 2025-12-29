# 🚀 HackerRank DSA Tutorials - Interactive Learning Resource

**Master Data Structures & Algorithms with step-by-step interactive tutorials**

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AmirCharkhi)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wvlt/hackerrank-dsa-tutorial)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amircharkhi)
[![HackerRank](https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white)](https://www.hackerrank.com/)

---

## 🤖 Automated Workflow - Quick Start

**📍 Run from this directory:** `/Volumes/X10 Pro/Youtube/Hackerrank_DSA/hackerrank-dsa-tutorial`

### Usage

```bash
# Navigate to the repository directory
cd "/Volumes/X10 Pro/Youtube/Hackerrank_DSA/hackerrank-dsa-tutorial"

# Preview changes (dry run)
python3 automate_tutorial_workflow.py VIDEO_ID --dry-run

# Apply changes
python3 automate_tutorial_workflow.py VIDEO_ID
```

### What It Does Automatically

1. **📹 Fetches Video Info** - Gets video title from YouTube
2. **🔍 Detects Problem** - Identifies which problem the video covers
3. **📝 Generates Files** - Creates comprehensive `.ipynb` and `.html` tutorial files with:
   - Problem statement with examples
   - Step-by-step solution explanation
   - Complete code implementation
   - Complexity analysis
   - Common pitfalls
   - Practice recommendations
4. **📝 Updates Mappings** - Updates `tutorial_mappings.yaml` in YouTube automation tool
5. **📦 Git Commit** - Commits new files to git
6. **☁️ Push to GitHub** - Pushes changes to remote repository
7. **📺 Update YouTube** - Runs `yt-auto process` to add tutorial links, description, chapters, and tags

### Example

```bash
# From the repository root directory:
python3 automate_tutorial_workflow.py LiX_wyuACwE --dry-run  # Preview
python3 automate_tutorial_workflow.py LiX_wyuACwE            # Apply
```

### Adding New Problems

When you create a video for a new problem, edit `automate_tutorial_workflow.py` and add to `PROBLEM_CONFIGS`:

```python
PROBLEM_CONFIGS = {
    "your problem name": {
        "num": 12,  # Next problem number
        "slug": "your_problem_slug",  # Filename slug (e.g., "delete_node")
        "name": "Your Problem Name",  # Display name
        "hackerrank_url": "https://www.hackerrank.com/challenges/...",
        "description": "Description of what this problem teaches"
    },
    # Add variations for better title matching
    "variation 1": { ... },  # Same config, different key
}
```

### Requirements

- Python 3.7+
- Git configured with remote repository
- `yt-auto` command available in PATH
- YouTube automation tool at: `/Users/amircharkhi/Documents/projects/agentic-ai/youtube-description-chapter-automation`

### Troubleshooting

**Problem Not Detected:**
- Add more variations to `PROBLEM_CONFIGS` in the script
- Check that keywords in video title match problem variations

**Git Push Fails:**
- Ensure you're authenticated with GitHub
- Verify remote: `git remote -v`

**YouTube Automation Fails:**
- Ensure `yt-auto` is installed and in PATH
- Check OAuth setup in YouTube automation directory

---

## 📚 About This Repository

This repository contains comprehensive, interactive tutorials for solving **HackerRank Data Structures & Algorithms problems**. Each problem includes:

- 📓 **Jupyter Notebook** - Detailed explanations with code examples and step-by-step solutions
- 🌐 **Interactive HTML Tutorial** - Step-by-step guided learning experience
- 💡 **Multiple Solution Approaches** - Learn different ways to solve problems
- ⏱️ **Complexity Analysis** - Understand time and space complexity
- 🎯 **Common Pitfalls** - Avoid mistakes others make

**Created by [Amir Charkhi](https://www.linkedin.com/in/amircharkhi) | [AI Tech Institute](https://github.com/wvlt/hackerrank-dsa-tutorial)**

---

## 📋 Problems Covered

| # | Problem | Notebook | Interactive Tutorial | HackerRank Link |
|---|---------|----------|---------------------|-----------------|
| 1 | Array DS - Reverse an Array | [📓](1_array_ds.ipynb) | [🌐](1_array_ds.html) | [🔗](https://www.hackerrank.com/challenges/arrays-ds/problem) |
| 2 | 2D Array DS - Hourglass Sum | [📓](2_2d_array_ds.ipynb) | [🌐](2_2d_array_ds.html) | [🔗](https://www.hackerrank.com/challenges/2d-array/problem) |
| 3 | Dynamic Array | [📓](3_dynamic_array.ipynb) | [🌐](3_dynamic_array.html) | [🔗](https://www.hackerrank.com/challenges/dynamic-array/problem) |
| 4 | Left Rotation | [📓](4_left_rotation.ipynb) | [🌐](4_left_rotation.html) | [🔗](https://www.hackerrank.com/challenges/array-left-rotation/problem) |
| 5 | Sparse Arrays | [📓](5_sparse_arrays.ipynb) | [🌐](5_sparse_arrays.html) | [🔗](https://www.hackerrank.com/challenges/sparse-arrays/problem) |
| 6 | Print Elements of Linked List | [📓](6_print_elements_of_linked_list.ipynb) | [🌐](6_print_elements_of_linked_list.html) | [🔗](https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem) |
| 7 | Insert Node at Tail | [📓](7_insert_a_node_at_the_tail.ipynb) | [🌐](7_insert_a_node_at_the_tail.html) | [🔗](https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem) |
| 8 | Insert Node at Head | [📓](8_insert_node_at_head.ipynb) | [🌐](8_insert_node_at_head.html) | [🔗](https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem) |
| 9 | Insert Node at Position | [📓](9_insert_node_position.ipynb) | [🌐](9_insert_node_position.html) | [🔗](https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem) |
| 10 | Delete Node | [📓](10_delete_node.ipynb) | [🌐](10_delete_node.html) | [🔗](https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem) |
| 11 | Reverse Linked List | [📓](11_reverse_linked_list.ipynb) | [🌐](11_reverse_linked_list.html) | [🔗](https://www.hackerrank.com/challenges/reverse-a-linked-list/problem) |

---

## 🚀 Getting Started

### Option 1: View Interactive Tutorials Online
1. Click on any HTML file (e.g., `1_array_ds.html`)
2. GitHub will render it - click "View Raw" or download to view interactively
3. Open the HTML file in your browser for the full interactive experience

### Option 2: Use Jupyter Notebooks
1. Clone this repository:
   ```bash
   git clone https://github.com/wvlt/hackerrank-dsa-tutorial.git
   cd hackerrank-dsa-tutorial
   ```
2. Install Jupyter Notebook:
   ```bash
   pip install jupyter notebook
   ```
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
4. Open any `.ipynb` file to start learning!

---

## 🎯 Learning Path

### Beginner Level
1. **Array DS** - Start here! Learn basic array operations
2. **Print Elements of Linked List** - Introduction to linked lists
3. **Left Rotation** - Array manipulation basics

### Intermediate Level
4. **2D Array DS** - Pattern recognition in matrices
5. **Sparse Arrays** - Hash map optimization
6. **Insert Node at Tail** - Linked list operations

### Advanced Level
7. **Dynamic Array** - XOR operations and complex indexing
8. **Insert Node at Head** - Efficient linked list operations
9. **Insert Node at Position** - Position-based insertion
10. **Delete Node** - Node deletion operations
11. **Reverse Linked List** - Three-pointer technique

---

## 💡 Key Features

### 📖 Comprehensive Explanations
- Step-by-step problem breakdown
- Visual demonstrations
- Multiple solution approaches
- Time and space complexity analysis

### 🎨 Interactive Learning
- Progress tracking
- Phase-based navigation
- Code reveals with syntax highlighting
- Insight boxes and tips

### 🔧 Practical Examples
- Real HackerRank problems
- Working code solutions
- Common pitfalls and how to avoid them
- Best practices

---

## 📺 Video Tutorials

Watch the complete video explanations on YouTube:

🎥 **[Subscribe to YouTube Channel](https://www.youtube.com/@AmirCharkhi)**

📺 **[HackerRank Solutions Playlist](https://www.youtube.com/playlist?list=PLV7y2_WFMCLKlGSC2Z-pZw1enbjeH7Hkq)**

---

## 📝 Topics Covered

- **Data Structures**: Arrays, 2D Arrays, Linked Lists, Hash Maps
- **Algorithms**: Array manipulation, Pattern recognition, Frequency counting, Linked list operations
- **Concepts**: Time complexity, Space complexity, Optimization techniques
- **Python**: Slicing, List operations, Dictionary operations, Object-oriented programming, Pointer manipulation

---

## 📚 Resources

- **HackerRank**: [Practice Problems](https://www.hackerrank.com/domains/data-structures)
- **YouTube**: [Amir Charkhi Channel](https://www.youtube.com/@AmirCharkhi)
- **LinkedIn**: [Connect with Amir](https://www.linkedin.com/in/amircharkhi)
- **GitHub**: [View Source Code](https://github.com/wvlt/hackerrank-dsa-tutorial)

---

## ⭐ Support This Project

<div align="center">

### **Help This Repository Grow!**

If these tutorials have helped you in your coding journey, please consider:

**⭐ Starring this repository** - Helps other learners discover quality DSA resources

**📤 Sharing with your network** - Spread the knowledge with friends, classmates, or colleagues

**💬 Providing feedback** - Open an issue or discussion to share your thoughts

**🎥 Subscribing to [YouTube Channel](https://www.youtube.com/@AmirCharkhi)** - Get notified of new video tutorials

**💼 Connecting on [LinkedIn](https://www.linkedin.com/in/amircharkhi)** - Join the community of learners

[![GitHub stars](https://img.shields.io/github/stars/wvlt/hackerrank-dsa-tutorial?style=for-the-badge)](https://github.com/wvlt/hackerrank-dsa-tutorial/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/wvlt/hackerrank-dsa-tutorial?style=for-the-badge)](https://github.com/wvlt/hackerrank-dsa-tutorial/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/wvlt/hackerrank-dsa-tutorial?style=for-the-badge)](https://github.com/wvlt/hackerrank-dsa-tutorial/watchers)

</div>

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🙏 Acknowledgments

- **HackerRank** for providing excellent coding challenges
- **Jupyter Notebook** for the amazing interactive learning platform
- **All learners** who use and improve these tutorials

---

<div align="center">

**Made with ❤️ by [Amir Charkhi](https://www.linkedin.com/in/amircharkhi) | [AI Tech Institute](https://github.com/wvlt/hackerrank-dsa-tutorial)**

**Subscribe to our [YouTube Channel](https://www.youtube.com/@AmirCharkhi) for more DSA tutorials! 🚀**

[⬆ Back to Top](#-hackerrank-dsa-tutorials---interactive-learning-resource)

</div>
