class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int m  = grid.length;
        int n = grid[0].length;

        if(m==0){
            return 0;
        }   

        int maxArea = 0;
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    int area = dfs(grid, i, j);
                    maxArea = Math.max(maxArea,area);
                }
            }
        }
        return maxArea;
    }

    public int dfs(int[][] grid, int start_r, int start_c){
        int m = grid.length;
        int n = grid[0].length;
        int [][]directions = {{0,1},{0,-1},{1,0},{-1,0}};
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{start_r,start_c});
        grid[start_r][start_c] = 0;
        int area = 0;
        while(!stack.isEmpty()){
            int[] coord = stack.pop();
            area += 1;
            for(int dir[] : directions){
                int nr = dir[0]+coord[0];
                int nc = dir[1]+coord[1];
                if(nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc]==1){
                    grid[nr][nc] = 0;
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        return area;
    }
}