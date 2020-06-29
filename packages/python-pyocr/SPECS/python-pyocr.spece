%global srcname pyocr

Name:           python-%{srcname}
Version:        0.7.2
Release:        6%{?dist}
Summary:        Python wrapper for OCR engines (Tesseract, Cuneiform, etc)

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/pyocr
# PyPI tarball does not include tests.
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/pyocr/-/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  tesseract
BuildRequires:  tesseract-osd
BuildRequires:  tesseract-langpack-fra
BuildRequires:  tesseract-langpack-jpn

%global _description \
A Python wrapper for Tesseract and Cuneiform

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)

Recommends:     tesseract

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
export LANG=C.UTF-8
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 \
    %{python3} -m pytest tests


%files -n python3-%{srcname}
%doc README.md AUTHORS ChangeLog html
%license COPYING
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Wed May 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-6
- Stop testing against now-unavailable cuneiform

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- Update to latest version

* Sun May 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7-1
- Update to latest version

* Sat Mar 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6-2
- Add documentation and licenses
- Cleanup shebangs

* Thu Mar 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6-1
- Initial package.
