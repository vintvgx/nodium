import React, { useRef, useCallback, FC, useEffect } from "react";
import EditorJS, { OutputData } from "@editorjs/editorjs";
import { EDITOR_JS_TOOLS } from "./Tools";
import "./Editor.css";

interface EditorProps {
  data: OutputData | undefined;
  setData: React.Dispatch<React.SetStateAction<OutputData | undefined>>;
}

const EditorJSTextBox: FC<EditorProps> = ({ data, setData }) => {
  const editorCore = useRef<EditorJS | null>(null);

  const handleInitialize = useCallback((instance: EditorJS) => {
    // Set reference to editor
    editorCore.current = instance;
  }, []);

  const handleSave = useCallback(async () => {
    // Retrieve data inserted
    const savedData = await editorCore.current?.save();
    // Save data
    if (savedData) {
      setData(savedData);
    }
  }, [setData]);

  useEffect(() => {
    const initializeEditor = async () => {
      if (!editorCore.current) {
        const editor = new EditorJS({
          holder: "editorjs",
          tools: EDITOR_JS_TOOLS,
          // autofocus: true,
          data: data ? data : undefined,
          placeholder: "Tell your story...",
          onReady: () => {
            console.log("Editor.js is ready to work!");
          },
        });
        handleInitialize(editor);
      }
    };

    initializeEditor();

    // // Cleanup on component unmount
    // return () => {
    //   if (editorCore.current) {
    //     editorCore.current.destroy();
    //   }
    // };
  }, [handleInitialize]);

  return (
    <>
      <div
        id="editorjs"
        className="max-w-full w-full min-h-screen"
        onBlur={handleSave}
      />
    </>
  );
};

export default EditorJSTextBox;
