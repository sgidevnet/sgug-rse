%global srcname behave

Name:           python-%{srcname}
Version:        1.2.6
Release:        7%{?dist}
Summary:        Tools for the behavior-driven development, Python style

License:        BSD
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/behave/behave/archive/v%{version}/%{srcname}-%{version}.tar.gz
# This patch is backport of upstream commits solving https://bugzilla.redhat.com/show_bug.cgi?id=1706085
# Upstream issue: https://github.com/behave/behave/issues/755
Patch0:         0001-Backport-for-py38-fixes.patch

BuildArch:      noarch

%?python_enable_dependency_generator

%global _description \
Behavior-driven development (or BDD) is an agile software development\
technique that encourages collaboration between developers, QA and non-\
technical or business participants in a software project.\
\
%{srcname} uses tests written in a natural language style, backed up\
by Python code.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-hamcrest
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-parse
BuildRequires:  python3-parse_type >= 0.4.2
BuildRequires:  python3-pytest
BuildRequires:  python3-six
Conflicts:      python2-behave < 1.2.6

%description -n python3-%{srcname} %{_description}

%package doc
Summary:        Documentation for %{name}
BuildRequires:  help2man
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-bootstrap-theme

%description doc %{_description}

This package contains documentation in reST and HTML formats and some
brief feature-examples.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build

make SPHINXBUILD=sphinx-build-3 html -C docs
rm -rf build/docs/html/.buildinfo


%install
mkdir -p %{buildroot}%{_mandir}/man1

%py3_install

PYTHONPATH=%{buildroot}%{python3_sitelib} help2man \
  --no-info \
  --name="Run a number of feature tests with behave." \
  --output=%{srcname}.1 \
  %{buildroot}%{_bindir}/%{srcname}

install -Dpm0644 %{srcname}.1 %{buildroot}%{_mandir}/man1/


%check
%{__python3} -m pytest -v


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%doc %{_mandir}/man1/%{srcname}.1*
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/setuptools_%{srcname}.py
%{python3_sitelib}/__pycache__/setuptools_%{srcname}.*


%files doc
%license LICENSE
%doc README.rst build/docs/html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-1
- Update to 1.2.6
- Drop python2 subpackage
- Drop downstream only patches adding functionality

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-24
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 1.2.5-23
- Fix python-behave obsoletes/provides

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.5-22
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-19
- Rebuild for Python 3.6

* Wed Sep 21 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-18.0.MC
- Rewrite the patch using six :(

* Tue Sep 20 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-18
- Add patch 0003-unicode_fixes.patch

* Fri Aug 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.2.5-17
- Modernize spec
- Backport patch to put label into sphinx before step

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-16
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-15
- Recover the build on RHEL-7 again.

* Wed Jun 22 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-14
- Add a symlink /usr/bin/behave unconditionally (fix #1348872)

* Fri Jun 03 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.2.5-13
- Update packaging to be compliant with new guidelines
- Fix building manpage
- Really run tests for python3
- Proper handling for binaries

* Wed Mar 23 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-12
- it works a way better when the symlink actually points to somewhere.

* Wed Mar 23 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-11
- /usr/bin/behave belongs to python2 package still (#1319632)

* Fri Mar 04 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-10
- Move python3 requires to python3 subpackage (#1314741)

* Mon Feb 29 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-9
- RHEL-7 doesn't have py3k toolchain.

* Mon Feb 29 2016 Matěj Cepl <mcepl@redhat.com> - 1.2.5-8
- Fix wrong %%if conditions.

* Thu Feb 25 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-7
- Make Python 3 the default version for the binary and provide a binary for 2 as well

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Björn Esser <besser82@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 03 2015 Matěj Cepl <mcepl@redhat.com> - 1.2.5-3
- Build also python3 packages (fix #1276923).

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Matej Cepl <mcepl@redhat.com> - 1.2.5-2
- Add a patch for embeding video in HTML formatted report

* Wed Apr 29 2015 Matej Cepl <mcepl@redhat.com> - 1.2.5-1
- Upgrade to the latest release (fix #1214767)

* Fri Sep 12 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.4-4
- Add another patch to fix an Unicode error (thanks for vbenes for
  fixing my earlier proposal).

* Thu Jul 17 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.4-2
- Build documentation even on EPEL-7.

* Thu Jun 19 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.4-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.3-13
- Remove bundled compatibility libraries and add Requires
  (fix #1096220).

* Mon Apr 07 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.3-12
- Add python-setuptools dependency (fix #1084996)

* Wed Mar 19 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.3-11
- Another fix for RHBZ# 1067388 by Vadim Rutkovsky

* Wed Mar 12 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.3-10
- Fix Patch 1

* Wed Mar 12 2014 Matěj Cepl <mcepl@redhat.com> - 1.2.3-9
- Add two patches provided by Vadim Rutkovsky (fix #1058371 and
  #1067388)

* Tue Oct 29 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-8
- Add Vadim Rutkovsky’s HTML Formatter patch (fix #1024023)

* Wed Oct 23 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-7
- Make generating of docs conditional again.

* Wed Oct 23 2013 Björn Esser <bjoern.esser@gmail.com> - 1.2.3-6
- fixed all remaining issues as mentioned in rhbz# 987622 c# 16
- added needed conditionals for building on el6.

* Tue Oct 22 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-5
- Generate sphinx documentation

* Tue Oct 22 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-4
- Fix spelling to en_US (apparently reviewer doesn't understand proper
  English ;))
- Add specific python2 marcros
- Fix files in _bindir to refer to python2 explicitly.
- Run testsuite

* Mon Oct 21 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-3
- Update generation of manpage from --help output.

* Sun Jul 28 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-2
- Fix changelog
- Give up on Python3 module ATM
  (https://bugzilla.redhat.com/show_bug.cgi?id=987622#c2 and
  https://github.com/behave/behave/issues/119)
- noarch package doesn't need CFLAGS set

* Tue Jul 23 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-1
- initial package for Fedora
