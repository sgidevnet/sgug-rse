%global srcname stem
%global _description\
Stem is a Python controller library that you can use to interact with Tor.\
With it you can write scripts and applications with capabilities similar\
to nyx.\
\
From a technical standpoint, Stem is a Python implementation of Tor's\
directory and control specifications.

Name:           python-stem
Version:        1.8.0
Release:        4%{?dist}
Summary:        Python controller library for Tor
# All source code is LGPLv3 except stem/util/ordereddict.py which is MIT
License:        LGPLv3 and MIT
URL:            https://stem.torproject.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
# https://www.torproject.org/docs/signing-keys.html.en
Source1:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz.asc

BuildArch:      noarch
BuildRequires:  python3-devel
# Doc building
BuildRequires:  python3-sphinx
# Testing
BuildRequires:  python3-mock
BuildRequires:  python3-crypto
BuildRequires:  python3-pytest-flakes
BuildRequires:  python3-pycodestyle

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package doc
Summary:        %{summary}

%description doc %_description

%prep
%autosetup -n %{srcname}-%{version} -p 1

%build
%py3_build
pushd docs
%make_build html
%make_build text
%make_build man
popd

%install
%py3_install
sed -e 's,^#!/usr/bin/python2$,#!/usr/bin/python3,' -i %{buildroot}%{_bindir}/tor-prompt
find docs/_build -name .buildinfo -delete
install -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
#%%{__python3} run_tests.py --unit

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/tor-prompt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info

%files doc
%doc README.md docs/_build/html docs/_build/text
%license LICENSE
%{_mandir}/man1/%{srcname}.1*

%changelog
* Sun May 31 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.8.0-4
- Disable tests for now (RHBZ#1797690)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.8.0-1
- Version 1.8.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.1-3
- Add patch to fix build on Python 3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.1-1
- Version 1.7.1

* Wed Oct 10 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.7.0-1
- Version 1.7.0
- Drop python2 subpackage
- Drop patch merged upstream
- Enable tests

* Tue Jul 17 2018 mh <mh+fedora@scrit.ch> - 1.6.0-5
- Make it build on python 3.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.6.0-1
- Version 1.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.5.4-3
- Python3 changes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.5.4-1
- Version 1.5.4

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-2
- Rebuild for Python 3.6

* Mon Nov 28 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.5.3-1
- Version 1.5.3

* Sat Feb 20 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-10
- Fix python3 shebang (RHBZ #1310323)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-8
- Disable ckecks again

* Mon Nov 30 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-7
- Re-enable checks
- Don't copy source to %%py3dir
- Leave only python3 version of tor-prompt script

* Wed Nov 25 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-6
- Checks are causing problems. Disable them for now.

* Wed Nov 25 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-5
- Rename file to python2-tor-prompt

* Tue Nov 24 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.1b-4
- Rebuild for Python 3.5 again

* Sun Nov 15 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-3
- Use python_provide macro
- Create symbolic links to tor-prompt

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1b-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1b-1
- Version 1.4.1b

* Mon May 18 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-1
- Version 1.4.1

* Wed May 13 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.0-2
- Skip integration tests

* Wed May 13 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.0-1
- Version 1.4.0

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.3.0-3
- Use license macro

* Wed Dec 24 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.3.0-2
- Run tests

* Tue Dec 23 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.3.0-1
- Version 1.3.0
- Add documentation in text format

* Sat Jun 14 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.2.2-2
- Rename tor-prompt to python3-tor-prompt in python3 subpackage

* Thu Jun 12 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.2.2-1
- Version 1.2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-2
- Rebuilt for F21 Python 3.4

* Sun Nov 10 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Version 1.1.1

* Tue Oct 15 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-1
- Version 1.1.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 28 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-4
- Enable parallel make

* Sun Apr 28 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-3
- Add doc subpackage

* Sun Apr 07 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-2
- Update Source URL

* Wed Mar 27 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.0.1-1
- Add python3 subpackage
- Update to 1.0.1

* Wed Mar 27 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.0.0-1
- Version 1.0.0

* Tue Feb 26 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 0-0.2.20130226gitbe9a532
- Update source code

* Sun Jan 13 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 0-0.1.20130113git
- Initial packaging
