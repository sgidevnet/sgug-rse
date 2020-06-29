%global srcname jenkins-job-builder

Name:           python-%{srcname}
Version:        3.2.0
Release:        2%{dist}
# Someone thought that 2.0.0.0b3 < 2.0.0
Epoch:          1
Summary:        Manage Jenkins jobs with YAML
License:        ASL 2.0
URL:            https://docs.openstack.org/infra/jenkins-job-builder/
Source:         %{pypi_source}

Patch0001: 0001-Re-order-some-XML-attributes-to-preserve-ordering.patch
Patch0002: 0002-conditional-publisher-sort-publisher-attributes-alph.patch

BuildArch:      noarch

%description
Jenkins Job Builder takes simple descriptions of Jenkins jobs in YAML format
and uses them to configure Jenkins. You can keep your job descriptions in
human readable text format in a version control system to make changes and
auditing easier. It also has a flexible template system, so creating many
similarly configured jobs is easy.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pbr) >= 1.8
# requirements.txt
BuildRequires:  python3dist(six) >= 1.9
BuildRequires:  (python3dist(pyyaml) >= 3.10 with python3dist(pyyaml) < 6)
BuildRequires:  python3dist(stevedore) >= 1.17.1
BuildRequires:  python3dist(python-jenkins) >= 0.4.15
BuildRequires:  python3dist(fasteners)
BuildRequires:  python3dist(jinja2)
# test-requirements.txt
BuildRequires:  python3dist(fixtures) >= 3
BuildRequires:  python3dist(testscenarios) >= 0.4
BuildRequires:  python3dist(testtools) >= 1.4
BuildRequires:  python3dist(mock) >= 2
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname}
Jenkins Job Builder takes simple descriptions of Jenkins jobs in YAML format
and uses them to configure Jenkins. You can keep your job descriptions in
human readable text format in a version control system to make changes and
auditing easier. It also has a flexible template system, so creating many
similarly configured jobs is easy.

%prep
%autosetup -n %{srcname}-%{version}%{?pre} -p1
rm -vr *.egg-info/

%build
export PBR_VERSION=%{version}
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v tests

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/jenkins-jobs
%{python3_sitelib}/jenkins_job_builder-*.egg-info/
%{python3_sitelib}/jenkins_jobs/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:3.2.0-2
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Ken Dreyer <ktdreyer@ktdreyer.com> 1:3.2.0-1
- Update to 3.2.0 (rhbz#1596891)
- Cherry-pick patches for py38 compat (rhbz#1706223)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.1-2
- Rebuilt for Python 3.8

* Tue Jul 30 07:34:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.0.1-1
- Update to 3.0.1

* Sat Jul 27 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.0.0-1
- Update to 3.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1:2.1.0-4
- Subpackage python2-jenkins-job-builder has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Apr 30 09:44:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.1.0-3
- Drop sphinx BRs (docs are not built)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 1:2.1.0-1
- Update to 2.1.0 (rhbz#1596891)
- Patch to Revert "Constrain PyYAML to v3.x."

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.0.10-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 1:2.0.10-1
- Update to 2.0.10 (rhbz#1591993)

* Fri Jun 01 2018 Ken Dreyer <ktdreyer@ktdreyer.com> 1:2.0.9-1
- Update to 2.0.9 (rhbz#1575169)

* Wed Apr 25 2018 Ken Dreyer <ktdreyer@ktdreyer.com> - 1:2.0.6-1
- Update to 2.0.6 (rhbz#1539219)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Aug 31 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.0.0.0-0.2.b2
- Add stevedore to Requires

* Thu Aug 31 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.0.0.0-0.1.b2
- Update to latest upstream tagged release (2.0.0.0 beta 2) (rhbz#1434196)
- Drop upstreamed patch
- Update URL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 06 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.4.0-6
- Backport patch to fix py3 version

* Tue Apr 05 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.4.0-5
- Use more python2- prefixed package in requires
- Simplify providing binary of jenkins-jobs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Paul Belanger <pabelanger@redhat.com> - 1.4.0-3
- Add Requires python-six (rhbz#1298324)

* Thu Jan 07 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.4.0-2
- Drop another Fedora 20 conditional (and implicitly add RHEL 7 support)
- Drop unneeded %%python_sitelib definition

* Tue Dec 29 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.4.0-1
- update to 1.4.0 (rhbz#1294527)

* Fri Dec 04 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.3.0-5
- Fix Requires on py2/py3 subpackages

* Thu Dec 03 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.3.0-4
- Patch to fix mavenName XML sorting on py35
- Make tests fail the build for py3
- Drop Fedora 20 conditionals

* Sat Nov 14 2015 Ken Dreyer <ktdreyer@ktdreyer.com>
- Fix FTBFS with Python 3.5
- Run tests on python3 (still fail due to mavenName XML sorting issue)
- rm Group tag
- Rename Python 2 subpackage to "python2-"
- Update for latest Python packaging guidelines
- Switch /usr/bin/jenkins-jobs to Python 3 on Fedora 24 and newer

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 27 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.3.0-1
- update to 1.3.0 (rhbz#1257377)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.2.0-1
- update to 1.2.0 (rhbz#1222209)

* Fri Apr 03 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.1.0-1
- update to 1.1.0
- rm python3_version compat macro; this has been defined since F13
- remove hard-coded srcname in some places
- add more test suite BRs
- run tests using py.test directly instead of setuptools
- add LICENSE

* Wed Nov 19 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.0.0-1
- update to 1.0.0
- rm argparse dep (this is in Python 2.7 core)
- Use PBR_VERSION instead of trying to avoid pbr.

* Wed Nov 19 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.9.0-0.20141111gitgbaff62b.1
- update to post-release git snapshot

* Tue Nov 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.9.0-1
- New package.
