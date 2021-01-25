import React from 'react';
import {
    Card, Spin,
    Tag, Col, Row, Typography,
    Switch
} from 'antd';

import AceEditor from "react-ace";
import "ace-builds/src-noconflict/theme-monokai";

class CodeViewer extends React.Component {
  state = {
      //file_path
      text_ed_theme: 'monokai',
      //themes:
      background_theme: "black",
      background_text_theme: 'white',
      // background_input_theme: '#2F3129',
      background_input_theme: '#282c34',
      background_output_theme: '#282c34',
      loading: true,
      codeview_code: null,
      placeholder_component: "Loading....",

      // Gutter
      gutterVisible: false
  }

  async componentDidMount() {
      console.log(this.props.file)
      if (!!this.props.file) {
          var fbase = this.props.file.split('/');
          fbase.pop();
          this.setState({
              fpath: this.props.file,
              fbase_path: fbase.join('/') + '/'
          })
          await fetch(this.props.file)
              .then((r) => r.text())
              .then(async (text) => {
                  try {
                      this.setState({
                          codeview_code: text,
                          loading: false,
                      })
                      console.log(this.state.notebook_json)
                  } catch (error) {
                      alert('OOps! Unable to load file')
                      this.setState({
                          codeview_code: { "message": "Unable to load file" },
                          loading: false,
                      })
                  }
              })
      }
  }

  render() {
    return (
        <div>
            <Spin spinning={this.state.loading} >
              <center>
                  {/* This is where the blog metadata and the cover will go */}
                  {
                      this.state.loading ? <div className="loading-state">Loading...</div> :
                                          <AceEditor
                                              readOnly
                                              placeholder="--"
                                              mode="python"
                                              theme={this.state.text_ed_theme}
                                              name="stdout"
                                              style={{
                                                  maxWidth: '850px',
                                                  padding: '10px',
                                                  margin: '10px 0px'
                                              }}
                                              width="100%"
                                              maxLines={this.state.codeview_code.split("\n").length}
                                              fontSize={14}
                                              showPrintMargin={false}
                                              showGutter={false}
                                              highlightActiveLine={false}
                                              value={this.state.codeview_code}
                                              setOptions={{
                                                  enableBasicAutocompletion: false,
                                                  enableLiveAutocompletion: false,
                                                  enableSnippets: false,
                                                  showLineNumbers: false,
                                                  tabSize: 2,
                                              }} />
                        }
                  </center>
              </Spin>
        </div>)
      }
    }

export default CodeViewer;
