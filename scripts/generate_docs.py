#!/usr/bin/env python3
"""
@DOC Documentation Auto-Generation Script
FE/BE 코드의 주석을 파싱하여 자동으로 문서 생성

사용법:
    python scripts/generate_docs.py

출력:
    docs/auto-generated.md
"""

import os
import re
from pathlib import Path
from datetime import datetime


class DocGenerator:
    """
    @DOC 문서 생성 클래스
    코드 파일에서 @FE, @BE, @DOC 주석을 추출하여 마크다운 문서 생성
    """

    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.fe_docs = []
        self.be_docs = []
        self.doc_docs = []

    def parse_file(self, filepath):
        """
        @DOC 파일 파싱 메서드
        Python, JavaScript, Vue 파일에서 주석 추출
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 주석 패턴 매칭
            patterns = {
                'FE': r'@FE\s+(.+?)(?=\n\s*(?:@|"""|\*/|-->))',
                'BE': r'@BE\s+(.+?)(?=\n\s*(?:@|"""|\*/|-->))',
                'DOC': r'@DOC\s+(.+?)(?=\n\s*(?:@|"""|\*/|-->))'
            }

            results = {}
            for tag, pattern in patterns.items():
                matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
                if matches:
                    results[tag] = matches

            return results

        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            return {}

    def scan_directory(self, directory, extensions):
        """
        @DOC 디렉토리 스캔 메서드
        지정된 확장자 파일들을 재귀적으로 검색
        """
        docs = []
        dir_path = self.project_root / directory

        if not dir_path.exists():
            return docs

        for ext in extensions:
            for filepath in dir_path.rglob(f"*{ext}"):
                relative_path = filepath.relative_to(self.project_root)
                parsed = self.parse_file(filepath)

                if parsed:
                    docs.append({
                        'file': str(relative_path),
                        'content': parsed
                    })

        return docs

    def generate_markdown(self):
        """
        @DOC 마크다운 생성 메서드
        추출된 주석을 마크다운 형식으로 변환
        """
        # 프론트엔드 스캔
        self.fe_docs = self.scan_directory('fe/src', ['.js', '.vue'])

        # 백엔드 스캔
        self.be_docs = self.scan_directory('be', ['.py'])

        # 스크립트 스캔
        self.doc_docs = self.scan_directory('scripts', ['.py'])

        # 마크다운 생성
        md_content = f"""# AI 기반 다국어 자동관리 웹시스템 - 자동 생성 문서

**생성 일시:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📘 Backend (FastAPI)

"""

        if self.be_docs:
            for doc in self.be_docs:
                md_content += f"\n### {doc['file']}\n\n"
                for tag, comments in doc['content'].items():
                    for comment in comments:
                        md_content += f"**@{tag}:** {comment.strip()}\n\n"
        else:
            md_content += "_백엔드 문서가 아직 없습니다._\n\n"

        md_content += "---\n\n## 💻 Frontend (Vue3)\n\n"

        if self.fe_docs:
            for doc in self.fe_docs:
                md_content += f"\n### {doc['file']}\n\n"
                for tag, comments in doc['content'].items():
                    for comment in comments:
                        md_content += f"**@{tag}:** {comment.strip()}\n\n"
        else:
            md_content += "_프론트엔드 문서가 아직 없습니다._\n\n"

        md_content += "---\n\n## 📚 Documentation Scripts\n\n"

        if self.doc_docs:
            for doc in self.doc_docs:
                md_content += f"\n### {doc['file']}\n\n"
                for tag, comments in doc['content'].items():
                    for comment in comments:
                        md_content += f"**@{tag}:** {comment.strip()}\n\n"
        else:
            md_content += "_문서 스크립트가 아직 없습니다._\n\n"

        return md_content

    def save_docs(self, output_path):
        """
        @DOC 문서 저장 메서드
        생성된 마크다운을 파일로 저장
        """
        markdown = self.generate_markdown()
        output_file = self.project_root / output_path

        # docs 디렉토리 생성
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"[OK] 문서가 생성되었습니다: {output_file}")
        print(f"   - Backend 파일: {len(self.be_docs)}개")
        print(f"   - Frontend 파일: {len(self.fe_docs)}개")
        print(f"   - Docs 파일: {len(self.doc_docs)}개")


def main():
    """
    @DOC 메인 실행 함수
    스크립트 실행 시 호출
    """
    # 프로젝트 루트 디렉토리 찾기
    current_dir = Path(__file__).parent.parent

    print("[시작] 문서 자동 생성 시작...")
    print(f"[경로] 프로젝트 루트: {current_dir}")

    # 문서 생성기 실행
    generator = DocGenerator(current_dir)
    generator.save_docs('docs/auto-generated.md')

    print("[완료] 문서 생성 완료!")


if __name__ == "__main__":
    main()
