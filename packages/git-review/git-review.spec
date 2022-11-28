# Enable Python 3 only for Fedora
%global with_python3 1

Name:		git-review
Version:	1.28.0
Release:	2%{?dist}
Summary:	A Git helper for integration with Gerrit

License:	ASL 2.0
URL:		https://github.com/openstack-infra/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch

%if 0%{?with_python3}
BuildRequires:	python3-devel
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%else
BuildRequires:	python2-devel
BuildRequires:	python2-pbr
BuildRequires:	python2-setuptools
%endif

Requires:	git
%if 0%{?with_python3}
Requires:	python3-requests
Requires:	python3-setuptools
%else
Requires:	python2-requests
Requires:	python2-setuptools
%endif

%description
An extension for source control system Git that creates and manages review
requests in the patch management system Gerrit. It replaces the rfc.sh script.

%prep
%setup -q

%build
%if 0%{?with_python3}
%py3_build
%else
%py2_build
%endif
sed -i 's/\r//' LICENSE

%install
%if 0%{?with_python3}
%py3_install
%else
%py2_install
%endif

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/

# We do not save ".gitreview" as dot.gitreview because the man page has it too.
# cp .gitreview #{buildroot}/usr/share/doc/dot.gitreview

install -p -m 0644 -D git-review.1 %{buildroot}%{_mandir}/man1/git-review.1

%files
%license LICENSE
%doc AUTHORS README.rst
%{_bindir}/git-review
%{_mandir}/man1/git-review.1.gz
# Our package name is git-review, but setup.py installs with underscore.
%if 0%{?with_python3}
%{python3_sitelib}/git_review/
%{python3_sitelib}/git_review-%{version}-py%{python3_version}*.egg-info/
%else
%{python2_sitelib}/git_review/
%{python2_sitelib}/git_review-%{version}-py%{python2_version}*.egg-info/
%endif

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Pete Zaitcev <zaitcev@redhat.com> - 1.28.0-1
- Update to 1.28.0 (required by gerrithub.io)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.26.0-2
- Rebuilt for Python 3.7

* Tue May 08 2018 Pete Zaitcev <zaitcev@redhat.com> - 1.26.0-1
- Update to 1.26.0 (#1564233)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Pete Zaitcev <zaitcev@redhat.com> - 1.25.0-7
- Fix crash with no_git_dir when using Python 3 (#1469831)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.25.0-5
- Rebuild for Python 3.6

* Wed Sep 14 2016 Pete Zaitcev <zaitcev@redhat.com> - 1.25.0-4
- Add Python 3 (#1322471)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Pete Zaitcev <zaitcev@redhat.com> - 1.25.0-1
- Upstream 1.25: the tracking branch workflow
- No more system-wide configuration in /etc

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Pete Zaitcev <zaitcev@redhat.com> - 1.24-5
- Add runtime requirement for setuptools to provide pkg_resources (#1214040)

* Thu Feb 05 2015 Pete Zaitcev <zaitcev@redhat.com> - 1.24-4
- Catch internal exceptions properly, avoid tripping abrtd (#1188913)

* Thu Dec 11 2014 Pete Zaitcev <zaitcev@redhat.com> - 1.24-3
- Fix up the man page (#1170410)

* Tue Nov 11 2014 Pete Zaitcev <zaitcev@redhat.com> - 1.24-2
- Require python-requests (#1162709)

* Wed Oct 29 2014 Pete Zaitcev <zaitcev@redhat.com> - 1.24-1
- Upstream 1.24: better deal w/ proxies, https; bugfixes (e.g. unicode crash)
- Checking for updates is out, other configuration options are in

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Pete Zaitcev <zaitcev@redhat.com>
- 1.22-1
- Upstream 1.22: per-user configurations, tweaks to gerrit branch search

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 Pete Zaitcev <zaitcev@redhat.com>
- 1.20-0.1
- Upstream 1.20: can have a file called "HEAD"; add -d option
- Patch the breakage with manpage in setup.py (temporarily - upstream pending)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.18-1
- Upstream 1.18: list actions

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.17-1
- Upstream 1.17: refs/publish, no ssh -Y, adapt to newer git so -d works

* Wed Apr 11 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.16-1
- Update to upstream 1.16: supports Gerrit 2.3 API (for draft reviews e.g.).

* Tue Apr 10 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.15-1
- Update to upstream 1.15: everything except the big refactor for OSX.

* Tue Feb 7 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.12-2
- Update with Rob Kukura's review comments: drop python_sitelib etc.

* Tue Jan 31 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.12-1
- Use upstream way to disable checking for updates; no more patching

* Wed Jan 18 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.9-4
- Strip CR characters from LICENSE at build time

* Tue Jan 17 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.9-3
- Update for Fedora packaging review

* Mon Jan 9 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.9-2
- Disable checking PyPi by default, add option -P to force it.

* Wed Jan 4 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.9-1

* Fri Dec 30 2011 Pete Zaitcev <zaitcev@redhat.com>
- 1.8-1
- New upstream version
- Build from original upstream tarball, do not repack

* Sat Dec 24 2011 Pete Zaitcev <zaitcev@redhat.com>
- 1.7-1
- Initial spec for Fedora
