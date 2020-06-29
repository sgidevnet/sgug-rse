%global         srcname  img2pdf
%global         desc   Python 3 library and command line utility img2pdf for losslessly converting\
a bunch of image files into a PDF file. That means that the images\
are either inserted into the PDF as-is or they are recompressed using\
lossless compression. Thus, img2pdf usually runs faster and may yield\
smaller PDF files than an ImageMagick convert command.\
\
The img2pdf command complements the pdfimages command.

Name:           python-%{srcname}
Version:        0.3.4
Release:        4%{?dist}
Summary:        Lossless images to PDF conversion library and command

License:        LGPLv3+
URL:            https://pypi.org/project/img2pdf
Source0:        %pypi_source

Patch0:         verbose-test.diff
# TODO remove with next upstream version
# cf. https://gitlab.mister-muffin.de/josch/img2pdf/commit/9d184ad0cdf50987ecae7f50a1c8189dbae30aae
Patch1:         test-magic.diff
# TODO remove with next upstream version
# cf. https://gitlab.mister-muffin.de/josch/img2pdf/commit/559d42cd4aed08333145c776878c7134bba2acf9
Patch2:         test-compress.diff

BuildArch:      noarch

# cf. Bug 1851638 - img2pdf fails to build on s390x because of issues in the ImageMagick dependency
# https://bugzilla.redhat.com/show_bug.cgi?id=1851638
ExcludeArch:    s390x

# required for test.sh
BuildRequires:  ImageMagick
BuildRequires:  ghostscript
BuildRequires:  libtiff-tools
BuildRequires:  mupdf
BuildRequires:  netpbm-progs
BuildRequires:  perl-Image-ExifTool
BuildRequires:  poppler-utils
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy

# other requirements
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


BuildRequires:  python3-pillow
BuildRequires:  python3-pdfrw

Requires:       python3-pillow

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
sed -i '1{/^#!\//d}' src/*.py
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test
bash -x test.sh

%files -n python3-%{srcname}
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-gui
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/jp2.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}-%{version}*.egg-info
%doc README.md


%changelog
* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-4
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-3
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-2
- Add upstream fix for test suite failure on aarch64

* Sun Apr 26 2020 Georg Sauthoff <mail@gms.tf> - 0.3.4-1
- Update to latest upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Georg Sauthoff <mail@gms.tf> - 0.3.2-2
- Fix unittest false-negatives on aarch64
* Sat Nov 24 2018 Georg Sauthoff <mail@gms.tf> - 0.3.2-1
- Update to latest upstream version
* Sat Aug 11 2018 Georg Sauthoff <mail@gms.tf> - 0.3.1-1
- Update to latest upstream version
* Wed Aug 1 2018 Georg Sauthoff <mail@gms.tf> - 0.3.0-1
- Update to latest upstream version
* Tue May 1 2018 Georg Sauthoff <mail@gms.tf> - 0.2.4-1
- initial packaging
