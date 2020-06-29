%global modname pyramid
%global sum The Pyramid web application framework, a Pylons project
%global desc Pyramid is a small, fast, down-to-earth, open source Python web development\
framework. It makes real-world web application development and deployment more\
fun, more predictable, and more productive.
%{?python_enable_dependency_generator}


Name:           python-%{modname}
Version:        1.10.4
Release:        7%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://trypyramid.com/
Source0:        %pypi_source %{modname}
BuildArch:      noarch



BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-hupper
BuildRequires:  python3-mako
BuildRequires:  python3-plaster
BuildRequires:  python3-plaster-pastedeploy
BuildRequires:  python3-setuptools
BuildRequires:  python3-translationstring
BuildRequires:  python3-venusian >= 1.0
BuildRequires:  python3-webtest
BuildRequires:  python3-zope-component >= 3.6.0
BuildRequires:  python3-zope-deprecation >= 3.5.0
BuildRequires:  python3-zope-interface

%if 0%{?fedora}
BuildRequires:  python3-webob >= 1.8.3
%else
BuildRequires:  python3-webob1.8 >= 1.8.3
%endif

%description
%{desc}


%package -n python3-pyramid
Summary:        %{sum}

%{?python_provide:%python_provide python3-pyramid}

Conflicts:      python2-pyramid < 1.10.4-4

%description -n python3-pyramid
%{desc}


%prep
%autosetup -n pyramid-%{version} -p1

# Remove bundled egg info
rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install

# Create the Python 3 executables.
for e in pcreate pserve prequest proutes pshell ptweens pviews pdistreport; do
    mv %{buildroot}/%{_bindir}/$e %{buildroot}/%{_bindir}/$e-%{python3_version};
    ln -s %{_bindir}/$e-%{python3_version} %{buildroot}/%{_bindir}/$e-3;
    ln -s %{_bindir}/$e-%{python3_version} %{buildroot}/%{_bindir}/$e
done;


%check
%{__python3} setup.py test


%files -n python3-pyramid
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*.egg-info
%{_bindir}/pcreate-%{python3_version}
%{_bindir}/pcreate-3
%{_bindir}/pcreate
%{_bindir}/pdistreport-%{python3_version}
%{_bindir}/pdistreport-3
%{_bindir}/pdistreport
%{_bindir}/prequest-%{python3_version}
%{_bindir}/prequest-3
%{_bindir}/prequest
%{_bindir}/proutes-%{python3_version}
%{_bindir}/proutes-3
%{_bindir}/proutes
%{_bindir}/pserve-%{python3_version}
%{_bindir}/pserve-3
%{_bindir}/pserve
%{_bindir}/pshell-%{python3_version}
%{_bindir}/pshell-3
%{_bindir}/pshell
%{_bindir}/ptweens-%{python3_version}
%{_bindir}/ptweens-3
%{_bindir}/ptweens
%{_bindir}/pviews-%{python3_version}
%{_bindir}/pviews-3
%{_bindir}/pviews

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-4
- Subpackage python2-pyramid has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-1
- Update to 1.10.4 (#1699203) to fix Python 3.8 test failures (#1698157)

* Tue Mar 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.10.2-1
- Update to 1.10.2.
- https://docs.pylonsproject.org/projects/pyramid/en/1.10-branch/changes.html

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.9.2-1
- Update to 1.9.2
- Require webob >= 1.7.0

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.9.1-7
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-5
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.9.1-4
- Use /usr/bin/python2 instead of /usr/bin/python when building.

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
