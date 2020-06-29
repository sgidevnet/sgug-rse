%global srcname sortedcontainers

Name:           python-%{srcname}
Version:        2.2.2
Release:        1%{?dist}
Summary:        Pure Python sorted container types

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
# PyPI tarball does not include docs or tests.
Source0:        https://github.com/grantjenks/python-sortedcontainers/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
SortedContainers is an Apache2 licensed sorted collections library, written in \
pure-Python, and fast as C-extensions.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%bcond_without tests
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
%endif

%bcond_without docs
%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(bm.sty)
%endif

%description -n python3-%{srcname} %{_description}


%package -n python-%{srcname}-doc
Summary:        %{summary}

%description -n python-%{srcname}-doc
Documentation for %{srcname} package.


%prep
%autosetup


%build
%py3_build

%if %{with docs}
pushd docs
make SPHINXBUILD=sphinx-build-%{python3_version} html
rm _build/html/.buildinfo
popd
%endif


%install
%py3_install


%if %{with tests}
%check
pushd tests
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    pytest-%{python3_version}
popd
%endif


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%if %{with docs}
%files -n python-%{srcname}-doc
%license LICENSE
%doc README.rst docs/_build/html
%endif


%changelog
* Mon Jun 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.2-1
- Update to latest version

* Sun Jun 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-8
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-7
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version

* Sat Oct 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.5-1
- Update to latest version

* Wed Oct 03 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.4-2
- Drop Python 2 subpackage.

* Thu Aug 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.4-1
- Update to latest version.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Sat May 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version.

* Sun Apr 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.10-1
- Update to latest version.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.9-1
- Update to latest version.

* Sun Sep 03 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-3
- Split out documentation subpackage.

* Sat Sep 02 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-2
- Shorten summary and description.
- Standardize spec a bit more.

* Mon Feb 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-1
- Initial package release.
