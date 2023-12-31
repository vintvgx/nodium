import { UserModel } from "./userModel";

export interface Topic {
  id: number;
  name: string;
}

export interface BlogContent {
  type: string;
  value?: string;
  level?: number;
  url?: string;
  alt?: string;
  caption?: string;
}

export interface BlogPost {
  id: number;
  user: UserModel | undefined;
  topic: Topic;
  title: string;
  content: string;
  created_at?: string | undefined;
  cover?: File | string | null;
}

export interface DispatchBlogPost {
  id: number;
  user: number;
  topic: number;
  title: string;
  content: string;
  created_at?: string | undefined;
  cover?: string | null;
}

export interface BlogPostData {
  topic: Topic;
  title: string;
  content: string;
  cover?: string | null;
  user: number;
}
