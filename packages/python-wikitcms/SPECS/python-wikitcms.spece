%global srcname wikitcms

Name:           python-%{srcname}
Version:        2.6.3
Release:        2%{?dist}
Summary:        Fedora QA wiki test management Python library

License:        GPLv3+
URL:            https://pagure.io/fedora-qa/python-wikitcms
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
python-wikitcms is a library for interacting with Fedora's wiki-based 'test
management' system. It can:

* Create the pages for release validation test events
* Find existing release validation event pages, in various ways
* Report test results

The wiki-based test management system itself is documented at:
https://fedoraproject.org/wiki/Wikitcms

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Obsoletes:      python2-%{srcname} < %{version}-%{release}
BuildRequires:  pyproject-rpm-macros
Recommends:     python3-openidc-client >= 0.4.0

%description -n python3-%{srcname}
python-wikitcms is a library for interacting with Fedora's wiki-based 'test
management' system. It can:

* Create the pages for release validation test events
* Find existing release validation event pages, in various ways
* Report test results

The wiki-based test management system itself is documented at:
https://fedoraproject.org/wiki/Wikitcms

This is the Python 3 build.

%prep
%autosetup -n %{srcname}-%{version}
# setuptools-git is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-git"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{srcname}
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.3-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Adam Williamson <awilliam@redhat.com> - 2.6.3-1
- New release 2.6.3: a couple of bug fixes

* Thu May 21 2020 Adam Williamson <awilliam@redhat.com> - 2.6.2-1
- New release 2.6.2: don't include src images in download tables

* Fri May 15 2020 Adam Williamson <awilliam@redhat.com> - 2.6.1-1
- New release 2.6.1: modernization, generic dist support
- Drop Python 2 builds and EPEL < 8 compat
- Use new pyproject macros

* Thu Apr 23 2020 Adam Williamson <awilliam@redhat.com> - 2.5.2-1
- New release 2.5.2: fix parsing test names with spaces

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Adam Williamson <awilliam@redhat.com> - 2.5.1-1
- New release 2.5.1: fix couple of bugs from 2.5.0

* Wed Nov 13 2019 Adam Williamson <awilliam@redhat.com> - 2.5.0-1
- New release 2.5.0: AMI info page generation

* Thu Sep 12 2019 Adam Williamson <awilliam@redhat.com> - 2.4.4-1
- New release 2.4.4: tweak weighting in image download table generation

* Mon Aug 26 2019 Adam Williamson <awilliam@redhat.com> - 2.4.3-1
- New release 2.4.3: avoid deprecation warnings with mwclient 0.10.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Adam Williamson <awilliam@redhat.com> - 2.4.2-1
- New release 2.4.2: fix a test bug exposed by the 2.4.1 bug fix

* Fri Nov 30 2018 Adam Williamson <awilliam@redhat.com> - 2.4.1-1
- New release 2.4.1: fix Current redirect page updates

* Thu Nov 22 2018 Adam Williamson <awilliam@redhat.com> - 2.4.0-2
- Disable Python 2 build on F30+, EL8+

* Sat Oct 06 2018 Adam Williamson <awilliam@redhat.com> - 2.4.0-1
- New release 2.4.0: drop old auth code

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Adam Williamson <awilliam@redhat.com> - 2.3.1-1
- New release 2.3.1: don't create events for updates composes

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.7 (F29+ only)

* Tue Feb 20 2018 Adam Williamson <awilliam@redhat.com> - 2.3.0-1
- New release 2.3.0: improved handling of candidate compose corner cases

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Adam Williamson <awilliam@redhat.com> - 2.2.2-1
- New release 2.2.2: avoid a harmless warning from mwclient sometimes

* Thu Nov 16 2017 Adam Williamson <awilliam@redhat.com> - 2.2.1-1
- New release 2.2.1: support OpenID Connect authentication
- Recommend openidc-client for openidc auth
- Update fedfind dependency

* Thu Oct 12 2017 Adam Williamson <awilliam@redhat.com> - 2.2.0-1
- New release 2.2.0: support Modular validation events

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Adam Williamson <awilliam@redhat.com> - 2.1.11-1
- New release 2.1.11: improve summary pages

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-2
- Rebuild for Python 3.6

* Fri Dec 16 2016 Adam Williamson <awilliam@redhat.com> - 2.1.10-1
- new release 2.1.10: drop some now-useless code and bump mwclient dependency

* Fri Dec 16 2016 Adam Williamson <awilliam@redhat.com> - 2.1.9-1
- new **SECURITY** release 2.1.9 (arbitrary code execution by evil wiki admin)
- 2.1.8 - minor refinements to fedfind usage

* Wed Nov 09 2016 Adam Williamson <awilliam@redhat.com> - 2.1.7-1
- new release 2.1.7 (convert 'Final' to 'RC' for >23)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 20 2016 Adam Williamson <awilliam@redhat.com> - 2.1.6-1
- new release 2.1.6 (re-add 'end' to TcmsPageList and generators)

* Fri Apr 08 2016 Adam Williamson <awilliam@redhat.com> - 2.1.5-1
- new release 2.1.5 (fix an issue with result row identification)

* Wed Mar 23 2016 Adam Williamson <awilliam@redhat.com> - 2.1.4-1
- new release 2.1.4 (drop a no-longer-needed workaround)
- enable tests

* Thu Mar 17 2016 Adam Williamson <awilliam@redhat.com> - 2.1.3-1
- new release 2.1.3 (adjust to fedfind / productmd changes)

* Wed Mar 16 2016 Adam Williamson <awilliam@redhat.com> - 2.1.2-1
- new release 2.1.2 (couple of bug fixes)

* Wed Mar 16 2016 Adam Williamson <awilliam@redhat.com> - 2.1.0-1
- new release 2.1.0 (more major Pungi 4-related changes)

* Fri Mar 04 2016 Adam Williamson <awilliam@redhat.com> - 2.0.2-1
- new release 2.0.2 (add a system-wide credentials file)

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 2.0.0-1
- new release 2.0.0
- Python 3 support added, python2-wikitcms / python3-wikitcms split

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Adam Williamson <awilliam@redhat.com> - 1.13.3-1
- new release 1.13.3: fix reporting results for similarly-named tests

* Tue Oct 27 2015 Adam Williamson <awilliam@redhat.com> - 1.13.2-1
- new release 1.13.2: fix triplet_sort when release is an int (relval)

* Mon Oct 26 2015 Adam Williamson <awilliam@redhat.com> - 1.13.1-1
- new release 1.13.1: another sorting fix

* Tue Oct 20 2015 Adam Williamson <awilliam@redhat.com> - 1.13-1
- new release 1.13: sorting improvements

* Sat Sep 19 2015 Adam Williamson <awilliam@redhat.com> - 1.12.3-1
- new release 1.12.3: use fedfind 'shortdesc' for download table
- requires fedfind >= 1.6 for shortdesc

* Thu Sep 17 2015 Adam Williamson <awilliam@redhat.com> - 1.12.2-1
- new release 1.12.2: drop a stray debug print, better wiki download tables
- Provides: python2-wikitcms
- requires fedfind >= 1.5.1 for the download table improvements

* Fri Aug 28 2015 Adam Williamson <awilliam@redhat.com> - 1.12.1-1
- new release 1.12.1: fix mwclient deprecation warning, minor updates

* Tue Jun 30 2015 Adam Williamson <awilliam@redhat.com> - 1.12-1
- new release 1.12: various bits added for Test Day handling

* Tue Apr 21 2015 Adam Williamson <awilliam@redhat.com> - 1.11.4-1
- new release 1.11.4: handling of 'bot' results (from automated test systems)

* Fri Apr 17 2015 Adam Williamson <awilliam@redhat.com> - 1.11.3-1
- new release 1.11.3: use system cached_property

* Thu Mar 26 2015 Adam Williamson <awilliam@redhat.com> - 1.11.2-1
- new release 1.11.2: bugfix (reporting multiple results to one row)

* Wed Mar 25 2015 Adam Williamson <awilliam@redhat.com> - 1.11.1-1
- new release 1.11.1: bugfix (affected relval size-check release guessing)

* Wed Mar 25 2015 Adam Williamson <awilliam@redhat.com> - 1.11-1
- new release 1.11: much more powerful result submission
- update description a bit

* Mon Mar 16 2015 Adam Williamson <awilliam@redhat.com> - 1.10.3-1
- new release 1.10.3: drop some unnecessary case normalization

* Wed Feb 18 2015 Adam Williamson <awilliam@redhat.com> - 1.10.2-1
- fix processing of Branched nightly pages

* Wed Feb 18 2015 Adam Williamson <awilliam@redhat.com> - 1.10.1-1
- revisions to event versioning, new get_validation_foo() methods, bugfixes

* Thu Feb 12 2015 Adam Williamson <awilliam@redhat.com> - 1.9.1-1
- new release 1.9.1: don't include a stray copy of fedfind

* Thu Feb 12 2015 Adam Williamson <awilliam@redhat.com> - 1.9-1
- new release 1.9: Download page creation, cleanups

* Wed Jan 07 2015 Adam Williamson <awilliam@redhat.com> - 1.8.4-1
- new release 1.8.4: fix page creation when no 'oldtext'

* Fri Jan 02 2015 Adam Williamson <awilliam@redhat.com> - 1.8.3-1
- new release 1.8.3: drop sanitization stuff (moved to relval), fix a bug

* Thu Jan 01 2015 Adam Williamson <awilliam@redhat.com> - 1.8.2-1
- new release 1.8.2: slightly stronger fix for last bug

* Thu Jan 01 2015 Adam Williamson <awilliam@redhat.com> - 1.8.1-1
- new release 1.8.1: serious security issue

* Tue Dec 23 2014 Adam Williamson <awilliam@redhat.com> - 1.8-1
- new release 1.8: multiple fixes and enhancements

* Fri Dec 19 2014 Adam Williamson <awilliam@redhat.com> - 1.7-1
- new release 1.7 (major overhaul)

* Tue Dec 16 2014 Adam Williamson <awilliam@redhat.com> - 1.6.1-1
- new release 1.6.1: revised nightly handling, bugfixes

* Tue Dec 09 2014 Adam Williamson <awilliam@redhat.com> - 1.5-1
- new release: nightly compose support

* Fri Oct 31 2014 Adam Williamson <awilliam@redhat.com> - 1.4.1-1
- new release (only enforces mwclient 0.7 dependency)

* Sat Oct 25 2014 Adam Williamson <awilliam@redhat.com> - 1.4-1
- new release 1.4 (API breaks all over)

* Fri Oct 24 2014 Adam Williamson <awilliam@redhat.com> - 1.3.1-1
- new release 1.3.1 (minor update)

* Tue Oct 21 2014 Adam Williamson <awilliam@redhat.com> - 1.3-1
- new release

* Thu Oct 16 2014 Adam Williamson <awilliam@redhat.com> - 1.2-1
- new release 1.2

* Mon Oct 13 2014 Adam Williamson <awilliam@redhat.com> - 1.1-1
- new release 1.1

* Mon Oct 06 2014 Adam Williamson <awilliam@redhat.com> - 1.0-1
- first build
