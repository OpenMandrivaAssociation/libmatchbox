%define	major	1
%define	libname	%mklibname mb %{major}
%define	devname	%mklibname -d mb

Summary:	Libraries for the Matchbox Desktop
Name:		libmatchbox
Version:	1.11
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://matchbox-project.org
Source0:	http://downloads.yoctoproject.org/releases/matchbox/libmatchbox/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libpng.patch
Patch1:		libmatchbox-1.9-underlinking.patch
BuildRequires:	jpeg-devel
BuildRequires:	Xsettings-client-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoxft)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xft)

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n	%{libname}
Libraries for the Matchbox Desktop.

%package -n	%{devname}
Group:		Development/C
Summary:	Static libraries and header files from %{name}
Provides:	matchbox-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
Static libraries and header files from %{name}.

%prep
%setup -q
%apply_patches
autoreconf -fiv

%build
%configure \
	--disable-static \
	--enable-xsettings \
	--enable-png \
	--enable-xft \
	--enable-jpeg \
	--enable-pango
%make CFLAGS="%{optflags} -Os `pkg-config --cflags pango pangoxft`"

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmb.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%dir %{_includedir}/libmb
%{_includedir}/libmb/*.h

