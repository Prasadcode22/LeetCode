// class Solution {
// public:
//     int lengthOfLastWord(string s) {
//         int count = 0;
//         bool wS = false;
//         for(int i = s.size()-1;i>=0;i--)
//         {
//             if(s[i] == ' ' && wS == false)
//             {
//                 continue;
//             }
//             else if(s[i] != ' ')
//             {
//                 count++;
//                 wS = true;
//             }
//             else{
//                 break;
//             }
//         }
//         return count;
//     }
// };