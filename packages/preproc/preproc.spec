# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python /usr/bin/python3
%else
%global python /usr/bin/python2
%endif

Name: preproc
Version: 0.2
Release: 2%{?dist}
Summary: Simple text preprocessor
License: GPLv2+
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#537a18ab6caac978885a509c76c11d269f30ccb1:preproc
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util/preproc
# git checkout preproc-0.2-1
# ./rpkg spec --sources
Source0: rpkg-util-preproc-537a18ab.tar.gz

BuildArch: noarch

%if 0%{?rhel} == 6
BuildRequires: python-argparse
Requires:      python-argparse
%endif

%description
Simple text preprocessor implementing a very basic templating language.
You can use bash code enclosed in triple braces in a text file and
then pipe content of that file to preproc. preproc will replace each of
the tags with stdout of the executed code and print the final renderred
result to its own stdout.

%prep
%setup -q -n rpkg-util-preproc

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 preproc %{buildroot}%{_bindir}

sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/preproc

install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/preproc.1 %{buildroot}%{_mandir}/man1

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{_bindir}/preproc
%{_mandir}/man1/preproc.1*

%changelog
* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.2-2
- rebuild because of koji break down

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.2-1
- encoding fixes
- make regular-expression only implementation
- add NOTE into help/man about usage of preproc on uknown files

* Tue Mar 03 2020 clime <clime@fedoraproject.org> 0.1-1
- use cmd_repr helper to properly render the executed command
- strip starting and ending whitespaces if any
- change to working email
- pass now required path to git_vcs macro in spec file
- source env before sourcing anything else
- fix spec files after CACHE to OUTPUT rename
- fix rpkg-util spec files
- build fix for rhel6
- provide man pages statically and add regen.sh
- add some explanation for tags matching
- allow multiple lines inside {{{}}}, fix expression for quoted
strings so that the closest quote is matched
- add missing BRs
- move preproc and rpkg macro defs into separate packages
