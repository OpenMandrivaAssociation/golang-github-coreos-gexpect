# http://github.com/coreos/gexpect
%global goipath         github.com/coreos/gexpect
Version:                0.1.1

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure golang expect library, for easily starting and controlling subprocesses
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/kballard/go-shellquote)
BuildRequires: golang(github.com/kr/pty)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENCE
%doc README.md

%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Release 0.1.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.10.20151125git5173270
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git5173270
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.20151125git5173270
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.20151125git5173270
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git5173270
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git5173270
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git5173270
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git5173270
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git5173270
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Mar 21 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git5173270
- First package for Fedora
  resolves: #1319724
